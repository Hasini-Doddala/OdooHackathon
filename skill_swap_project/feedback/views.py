from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from swaps.models import SwapRequest
from .forms import FeedbackForm
from .models import Feedback

@login_required
def give_feedback(request, swap_id):
    print("📢 Feedback view loaded!") 
    swap = get_object_or_404(SwapRequest, id=swap_id)

    # Only allow feedback if swap is accepted and user is involved
    if swap.status != 'accepted' or request.user not in [swap.sender, swap.receiver]:
        return redirect('manage_requests')

    # Prevent duplicate feedback
    if Feedback.objects.filter(swap=swap, reviewer=request.user).exists():
        return redirect('manage_requests')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.swap = swap
            feedback.reviewer = request.user
            feedback.save()
            return redirect('manage_requests')
    else:
        form = FeedbackForm()

    return render(request, 'feedback/give_feedback.html', {'form': form, 'swap': swap})

# Create your views here.
