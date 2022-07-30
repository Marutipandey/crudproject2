from django.urls import URLPattern, path
from . import views
urlpatterns=[
path('services/',views.services,name='services')
]