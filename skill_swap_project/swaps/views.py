from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from skills.models import Skill
from .models import SwapRequest
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

@login_required
def send_swap_request(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)

    if request.method == 'POST':
        offered_skill_id = request.POST.get('offered_skill')
        wanted_skill_id = request.POST.get('wanted_skill')

        offered_skill = Skill.objects.get(id=offered_skill_id)
        wanted_skill = Skill.objects.get(id=wanted_skill_id)

        SwapRequest.objects.create(
            sender=request.user,
            receiver=receiver,
            offered_skill=offered_skill,
            wanted_skill=wanted_skill
        )
        return HttpResponse("✅ Swap request sent successfully!")  # you can customize this

    return render(request, 'swaps/send_swap.html', {
        'receiver': receiver,
        'offered_skills': request.user.profile.skills_offered.all(),
        'wanted_skills': receiver.profile.skills_wanted.all(),
    })

@login_required
def manage_requests(request):
    sent_requests = SwapRequest.objects.filter(sender=request.user)
    received_requests = SwapRequest.objects.filter(receiver=request.user)

    return render(request, 'swaps/manage_requests.html', {
        'sent_requests': sent_requests,
        'received_requests': received_requests,
    })

@login_required
def update_swap_status(request, swap_id, action):
    swap = get_object_or_404(SwapRequest, id=swap_id)

    if action == 'accept' and swap.receiver == request.user:
        swap.status = 'accepted'
        swap.save()
        messages.success(request, "Swap accepted!")

    elif action == 'reject' and swap.receiver == request.user:
        swap.status = 'rejected'
        swap.save()
        messages.error(request, "Swap rejected.")

    elif action == 'cancel' and swap.sender == request.user and swap.status == 'pending':
        swap.status = 'cancelled'
        swap.save()
        messages.warning(request, "Swap cancelled.")

    return redirect('manage_requests')

# Create your views here.
