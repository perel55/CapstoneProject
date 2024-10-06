from django.db import models

# Create your models here.

class Residents(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(max_length=255)
    phone_number = models.CharField(max_length=255)
    picture = models.ImageField(upload_to = 'images/', null=True)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname} {self.postion}"

class Personnel(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(max_length=255)
    phone_number = models.CharField(max_length=255)
    picture = models.ImageField(upload_to = 'images/', null=True)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname} {self.postion}"
class Bhw(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    zone = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    birthdate = models.DateField(max_length=255)
    phone_number = models.CharField(max_length=255)
    picture = models.ImageField(upload_to = 'images/', null=True)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname} {self.postion}"

 

class Account_Type(models.Model):
    Account_type = models.CharField(max_length =255)
    
    def __str__(self):
        return f"{self.Account_type}"

class Accounts(models.Model):
    bhw_id= models.ForeignKey(Bhw, on_delete=models.CASCADE, null=True)
    officials_id= models.ForeignKey(Personnel, on_delete=models.CASCADE, null=True)
    resident_id= models.ForeignKey(Residents, on_delete=models.CASCADE, null=True)
    account_typeid= models.ForeignKey(Account_Type, on_delete=models.CASCADE, null=True)