from django.urls import path

from userapp import views

urlpatterns = [
    path('user/',views.user),
    path('users/',views.UserView.as_view()),
    path('users/<str:pk>/',views.UserView.as_view()),
    path('api_users/',views.UserAPIView.as_view()),
    path('api_users/<str:pk>/',views.UserAPIView.as_view())
]