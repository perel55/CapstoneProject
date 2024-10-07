from django.contrib import admin
from .models import Accounts, Residents, Bhw, Account_Type, Personnel

# Register your models here.
admin.site.register(Accounts)
admin.site.register(Residents)
admin.site.register(Bhw)
admin.site.register(Account_Type)
admin.site.register(Personnel)

