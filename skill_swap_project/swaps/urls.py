from django.urls import path
from . import views

urlpatterns = [
    # Define user-related paths later
    # Example:
    # path('profile/', views.profile_view, name='profile'),
     path('send/<int:receiver_id>/', views.send_swap_request, name='send_swap'),
     path('manage/', views.manage_requests, name='manage_requests'),
     path('update/<int:swap_id>/<str:action>/', views.update_swap_status, name='update_swap'),
]
