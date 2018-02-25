from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import User

def index(request):
    if 'login' not in request.session: #fresh visit
        request.session['login'] = False
        request.session.pop('user')

    if request.session['login'] == True:
        return redirect(reverse('wall:secrets'))
    else:
        return render(request, "secrets/index.html")

def register(request):
    if request.session['login'] == True:
        return redirect(reverse('wall:secrets'))
    else:
        errors = User.objects.user_validator(request.POST)
        if len(errors):
            for key, error in errors.iteritems():
                messages.error(request, error)
            return redirect(reverse('secrets:index'))
        else:
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=User.objects.hash_new_PW(request.POST['password']),
            )
            request.session['user'] = user.first_name
            request.session['user_id'] = user.id
            request.session['login'] = True
            return redirect(reverse('wall:secrets'))

def login(request):
    if request.session['login'] == True:
        return redirect(reverse('wall:secrets'))
    else:
        tryMe = User.objects.try_by_email(request.POST)
        # gets the User object back if the email and password validate...
        # otherwiae it gets back a library of errors messages.
        if type(tryMe) == User:
            request.session['user'] = tryMe.first_name
            request.session['user_id'] = tryMe.id
            request.session['login'] = True
            return redirect(reverse('wall:secrets'))
        else:
            if len(tryMe):
                for key, error in tryMe.iteritems():
                    messages.error(request, error)
            return redirect(reverse('secrets:index'))

def logout(request):
    messages.error(request, "Goodbye, "+ request.session['user'] +". You are now loged out." )
    request.session.pop('login')
    return redirect(reverse('secrets:index'))
