from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Request, Services, Residents
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



def residentSchedule(request):
    profile_picture = request.session.get('profile_picture', None)
    account_type = request.session.get('account_type', None)

    return render(request, 'resident/residentCalendar.html', {
        'profile_picture': profile_picture,
        'account_type': account_type
    })


@login_required
def ScheduleView(request):
    services = Services.objects.all()  # Fetch all services
    if request.method == "POST":
        service_id = request.POST.get('service-id')
        reason = request.POST.get('reason')
        total_price = request.POST.get('total-price')
        schedule_date = request.POST.get('schedule-date')
        schedule_start_time = request.POST.get('schedule-start-time')
        schedule_end_time = request.POST.get('schedule-end-time')

        # Ensure the service exists before creating the request
        service = Services.objects.get(service_id=service_id)

        # Check if the user has a related resident profile
        try:
            resident = request.user.residents
        except Residents.DoesNotExist:
            messages.error(request, "You must complete your profile before making a request.")
            return redirect('ScheduleView')

        new_request = Request(
            Resident_id=resident,  # Use the correct resident object
            service_id=service,
            reason=reason,
            total_price=total_price,
            schedule_date=schedule_date,
            schedule_start_time=schedule_start_time,
            schedule_end_time=schedule_end_time
        )
        new_request.save()

        return redirect('ScheduleView')  # Redirect to the same view after saving

    return render(request, 'resident/userd.html', {
        'services': services
    })



@csrf_exempt
def get_events(request):
    events = Request.objects.all()
    event_data = []
    for event in events:
        event_data.append({
            'id': event.id,
            'title': event.service_id.service_name,
            'start': f"{event.schedule_date}T{event.schedule_start_time}",
            'end': f"{event.schedule_date}T{event.schedule_end_time}",
            'extendedProps': {
                'schedule_id': event.id,
                'schedule_type': 'Not-Available',  # Assuming it's not available for booking after scheduling
            }
        })
    return JsonResponse(event_data, safe=False)

class ScheduleDataView(View):
    def get(self, request):
        today = datetime.now().date()
        schedules = Request.objects.filter(schedule_date__gte=today)
        events = []

        for schedule in schedules:
            start = f"{schedule.schedule_date}T{schedule.schedule_start_time}"
            end = f"{schedule.schedule_date}T{schedule.schedule_end_time}"
            events.append({
                'title': str(schedule.service_id.name),  # Assuming `service_id` has a `name` attribute.
                'start': start,
                'end': end,
                'extendedProps': {
                    'schedule_type': schedule.service_id.name,
                    'schedule_id': schedule.id,
                    'schedule_date': schedule.schedule_date.isoformat(),
                },
            })

        return JsonResponse(events, safe=False)

