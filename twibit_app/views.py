from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from twibit_app.forms import AuthenticateForm, UserCreateForm, TwibitForm
from models import Twibit
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request, auth_form=None, user_form=None):
    #User is logged in
    if request.user.is_authenticated():
        twibit_form = TwibitForm()
        user = request.user
        twibits_self = Twibit.objects.filter(user=user.id)
        twibits_buddies = Twibit.objects.filter(user__userprofile__in=user.profile.follows.all)
        twibits = twibits_self | twibits_buddies

        return render(request,
            'buddies.html',
            {'twibit_form': twibit_form, 'user': user, 'twibits': twibits, 'next_url': '/'})

    else:
        #User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()

        return render(request,
            'home.html',
            {'auth_form': auth_form, 'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

@login_required
def submit(request):
    if request.method == 'POST':
        twibit_form = TwibitForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if twibit_form.is_valid():
            twibit = twibit_form.sava(commit=False)
            twibit.user = request.user
            twibit.save()
            return redirect(next_url)
        else:
            return public(request, twibit_form)
    return redirect('/')

@login_required
def public(request, twibit_form=None):
	twibit_form = twibit_form or TwibitForm()
	twibits = Twibit.objects.reverse()[:10]
	return render(request,
		'public.html',
		{'twibit_form': twibit_form, 'next_url': '/twibits', 'twibits': twibits, 'username': request.user.username})


