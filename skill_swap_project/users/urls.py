from django.urls import path
from . import views

urlpatterns = [
    # Define user-related paths later
    # Example:
    # path('profile/', views.profile_view, name='profile'),
    path('profile/', views.profile_view, name='profile'),
]
