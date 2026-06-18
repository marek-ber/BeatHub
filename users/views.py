from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings

from .forms import ProfileForm, RegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    playlists = profile_user.playlists.all()

    return render(
        request,
        "users/profile.html",
        {
            "profile_user": profile_user,
            "playlists": playlists,
        }
    )


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect(
                "profile",
                username=request.user.username
            )

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "users/edit_profile.html",
        {"form": form}
    )

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            send_mail(
                subject="Witamy w BeatHub",
                message=(
                    f"Cześć {user.username}!\n\n"
                    "Twoje konto w BeatHub zostało utworzone.\n"
                    "Możesz teraz tworzyć playlisty i odkrywać muzykę."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {"form": form}
    )