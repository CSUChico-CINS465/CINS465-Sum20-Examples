from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:page>/', views.index),
    path('second/', views.view_two),
]