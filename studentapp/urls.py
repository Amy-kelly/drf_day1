from django.urls import path

from studentapp import views

urlpatterns = [
    path("stu/",views.StudentAPIView.as_view()),
    path("stu/<str:pk>/",views.StudentAPIView.as_view()),
]