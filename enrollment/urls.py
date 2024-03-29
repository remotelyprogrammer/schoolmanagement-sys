from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.CreateEnrollmentView.as_view(), name='enrollment-create'),
]