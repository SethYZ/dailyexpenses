from django.shortcuts import render,redirect
from .forms import RegisterForm, ProfileUpdateForm, UserInfoUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully!')
            return redirect('main-home')

    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserInfoUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Account profile has been updated!')
            return redirect('main-index')
        elif p_form.is_valid():
            p_form.save()
            messages.success(request, f'Account profile has been updated!')
            return redirect('main-index')
        elif u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account profile has been updated!')
            return redirect('main-index')

    else:
        u_form = UserInfoUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'register/profile.html', context)
