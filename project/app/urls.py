from django.urls import path
from . import views

urlpatterns = [
    path('csv-file/', views.ClientView.as_view(), name='cvs-file'),
]

