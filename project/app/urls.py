from django.urls import path
from . import views

urlpatterns = [
    path('cvs-file/', views.ClientView.as_view(), name='cvs-file'),
]

