from django.urls import URLPattern, path
from . import views
urlpatterns=[
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
]