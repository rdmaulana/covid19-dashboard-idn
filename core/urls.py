from django.contrib import admin
from django.urls import path

from core import views as page

urlpatterns = [
	path('', page.dashboard, name='dashboard'),
]
