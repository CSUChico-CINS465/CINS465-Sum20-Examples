from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
    path('second/', views.view_two),
    path('suggestions/', views.get_suggestions),
    path('suggestion/', views.add_suggestion),
    path('comment/<int:sugg_id>/', views.add_comment),
]
