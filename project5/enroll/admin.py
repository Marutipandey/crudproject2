from django.contrib import admin

from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("Question","Choice1","Choice2","Choice3","Choice4","Right_Choice")


    
    