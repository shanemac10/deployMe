from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..secrets.models import User
from models import Secret

def secrets(request):
    if request.session['login'] == True:
        request.session['where_I_came_from'] = 'wall:secrets'
        this_user = User.objects.get(id=request.session['user_id'])
        new_secrets = Secret.objects.order_by("-created_at")[:5]
        # for secret in new_secrets:
        #     secret.liked_by_this_user = Secret.objects.if_liked(secret,this_user)

        context = {
            "new_secrets" : new_secrets,
            "user": this_user
        }
        return render(request, 'wall/secrets.html', context)
    else:
        return redirect(reverse('secrets:index'))

def supersecrets(request):
    if request.session['login'] == True:
        request.session['where_I_came_from'] = 'wall:supersecrets'
        this_user = User.objects.get(id=request.session['user_id'])
        super_secrets = Secret.objects.order_by("-like_count")[:5]
        # for secret in super_secrets:
        #      secret.liked_by_this_user = Secret.objects.if_liked(secret,this_user)

        context = {
            "super_secrets" : super_secrets,
            "user": this_user
        }
        return render(request, 'wall/supersecrets.html', context)
    else:
        return redirect(reverse('secrets:index'))

def tell(request):
    if request.session['login'] == True:
        secret = Secret.objects.create(
            the_secret=request.POST['the_secret'],
            the_user= User.objects.get(id=request.session['user_id'])
        )
        secret.save()
        return redirect(reverse(request.session['where_I_came_from']))
    else:
        return redirect(reverse('secrets:index'))

def like(request, secret_id):
    if request.session['login'] == True:
        this_secret = Secret.objects.get(id=secret_id) #get the secret object itself
        result = Secret.objects.like(this_secret, request.session['user_id']) #call it's like method
        print result
        this_secret.liked_by_this_user = result
        return redirect(reverse(request.session['where_I_came_from']))
    else:
        return redirect(reverse('secrets:index'))

def delete(request, secret_id):
    if request.session['login'] == True:
        this_secret = Secret.objects.get(id=secret_id) #get the secret object itself
        result = Secret.objects.delete(this_secret, request.session['user_id']) #call it's like method
        print result
        return redirect(reverse(request.session['where_I_came_from']))
    else:
        return redirect(reverse('secrets:index'))
