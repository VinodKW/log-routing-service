from django.urls import path
from . import views

urlpatterns = [
    path('log',views.create_log),
]