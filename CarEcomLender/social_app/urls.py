from django.urls import path

from . import views

urlpatterns = [
    path('/api/user/', views.UserListCreate.as_view() ),
    path('/api/user/update', views.UserListUpdate.as_view()),

]
