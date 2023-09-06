from django.contrib import admin
from django.urls import path
from .views import register_user_view




urlpatterns = [
    path('registeruser/',view=register_user_view , name='registeruser'),

]
