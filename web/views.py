from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from web.forms import TeamForm, ManageTeamForm
from web.models import Team

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
    if request.method == 'POST' and 'register' in request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.password = make_password(form.cleaned_data['password'])
            team.save()
            return HttpResponseRedirect('/') # TODO: Thanks for registration page
    elif request.method == 'POST' and 'signin' in request.POST:
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
        form = TeamForm()
    return render(request, 'register.html', {'form': form})

def signout(request):
    request.session['team'] = None
    logout(request)
    return HttpResponseRedirect('/')

def manage(request):
    if request.session.get('team') is None:
        return HttpResponseRedirect('/register')
    else:
        team = Team.objects.get(name = request.session.get('team'))
        form = ManageTeamForm(instance=team)
        if request.method == 'POST':
            form = ManageTeamForm(request.POST, instance=team)
            if form.is_valid():
                team.name = form.cleaned_data['name']
                team.password = make_password(form.cleaned_data['password'])
                team.member_1 = form.cleaned_data['member_1']
                team.member_2 = form.cleaned_data['member_2']
                team.member_3 = form.cleaned_data['member_3']
                team.member_4 = form.cleaned_data['member_4']
                team.email_1 = form.cleaned_data['email_1']
                team.email_2 = form.cleaned_data['email_2']
                team.email_3 = form.cleaned_data['email_3']
                team.email_4 = form.cleaned_data['email_4']
                team.size_1 = form.cleaned_data['size_1']
                team.size_2 = form.cleaned_data['size_2']
                team.size_3 = form.cleaned_data['size_3']
                team.size_4 = form.cleaned_data['size_4']
                team.diet = form.cleaned_data['diet']
                team.save()
                return HttpResponseRedirect('/manage') # TODO: Thanks for registration page
        else:
            form = ManageTeamForm(instance=team)
    return render(request, 'manage.html', {'form': form})
