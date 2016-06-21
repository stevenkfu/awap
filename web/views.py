from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from web.forms import TeamForm

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.password = make_password(form.cleaned_data['password'])
            team.save()
            return HttpResponseRedirect('/') # TODO: Thanks for registration page
    else:
        form = TeamForm()
    return render(request, 'register.html', {'form': form})

def signout(request):
    request.session['team'] = None
    logout(request)
    return HttpResponseRedirect('/')
