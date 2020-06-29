from django.urls import path

from staffapp import views

urlpatterns = [
    path("emp/",views.EmployeeAPIView.as_view()),
    path("emp/<str:pk>/",views.EmployeeAPIView.as_view()),
]