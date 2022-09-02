from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Journal
from django.contrib.auth import login, authenticate, logout


def index(request):
    return render(request, 'base.html')

# Display all journal entries from current user
def home(request):
    this_user = User.objects.get(id=request.user.id)
    journals = Journal.objects.filter(user=this_user)
    context = {
        'journals' : journals
    }
    return render(request, 'home.html', context)

# Register user account
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})

# Log in user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Unable to log in. Please try again.')
            return redirect('login_user')
    else:
        return render(request, 'account/login.html')

# Log out user
def logout_user(request):
    logout(request)
    return redirect('index')

# Create a journal entry
def create_journal(request):
    this_user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        Journal.objects.create(title=request.POST['title'], content=request.POST['content'], user=this_user)
        return redirect('home')
    return render(request, 'journal/create_journal.html')

# Open up journal entry page
def read_entry(request, id):
    entry = Journal.objects.get(id=id)
    context = {
        'entry': entry
    }
    return render(request, 'journal/read_entry.html', context)

# Delete an entry
def delete_entry(request, id):
    entry = Journal.objects.get(id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    context = {
        'entry': entry
    }
    return render(request, 'journal/delete_entry.html', context)

# Update a journal entry 
def update(request, id):
    context = {
        'entry': Journal.objects.get(id=id)
    }
    return render(request, 'journal/update_entry.html', context)

# Submit the journal update
def update_entry(request, id):
    if request.method == "POST":
        entry = Journal.objects.get(id=id)
        entry.title = request.POST.get('title')
        entry.content = request.POST.get('content')
        entry.save()
        return redirect(f'/read_entry/{id}')

# Display user info
def view_account(request):
    return render(request, 'account/view_account.html')

# Change password for user account
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Unable to update password. Please try again.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

# Submit password change
def success(request):
    return render(request, 'account/success.html')

