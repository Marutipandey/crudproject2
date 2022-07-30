from django.contrib import admin
from enroll.models import Student
from .forms import StudentRegistration
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','studenttpassword','studenttname','studenttemail')



    











