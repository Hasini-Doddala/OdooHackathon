from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'profile': profile})

# Create your views here.
