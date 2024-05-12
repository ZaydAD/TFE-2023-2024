from django.shortcuts import render, redirect
from .models import Profile, Friend, Messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def home(request):
    user = request.user.profile
    friends = user.friends.all()
    context = {"user": user, "friends": friends}
    return render(request, "home.html", context)

@login_required
def chat(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    context = {"friend": friend}
    return render(request, "chat.html", context)

@login_required
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("update_profile")

    context = {"form": form}
    return render(request, "update_profile.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, "Invalid username or password.")
    return render(request, 'user_login.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created ! You can now log in.')
            return redirect('user_login')
    else:
        form = UserForm()

    context = {"form": form}
    return render(request, 'register.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


def Messages(request): #Unfinished function.

    if request.method == 'POST':
        sender_id = request.POST.get('sender')
        receiver_id = request.POST.get('receiver')
        message_text = request.POST.get('message')
        
        sender = Profile.objects.get(id=sender_id)
        receiver = Profile.objects.get(id=receiver_id)
        
        Messages.objects.create(sender=sender, receiver=receiver, message=message_text)
        return redirect('chat.html')  # Redirect after POST
    else:
        profiles = Profile.objects.all()
        return render(request, 'chat.html', {'profiles': profiles})