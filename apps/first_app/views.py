from django.shortcuts import render,redirect

from django.contrib import messages

from .models import User

# Create your views here.

def index(request):
    return render(request,"first_app/index.html")


def register(request):
    if request.method == 'POST':
        response_from_models = User.objects.register(request.POST)

        if response_from_models['status'] == True:
            request.session['user_id'] = response_from_models['user'].id
            return redirect("newsfeed:success")
        else:
            for error in response_from_models['errors']:
                messages.error(request,error)
                return redirect('loginreg:index')

def login(request):
    if request.method == 'POST':
        response_from_models = User.objects.login(request.POST)

        if response_from_models['status']:
            request.session['user_id'] = response_from_models['user'].id

            return redirect("newsfeed:success")
        else:
            messages.error(request, response_from_models['errors'])
            return redirect('loginreg:index')

def logout(request):
    request.session.clear()
    return redirect('loginreg:index')