from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django_tables2 import RequestConfig

from web.forms import TeamForm, ManageTeamForm
from web.models import Team
from web.tables import TeamScoreboard

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
            messages.error(request, 'Invalid team name or password')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def register(request):
    if request.session.get('team', None) is not None:
        messages.error(request, 'Please delete your team to create a new team')
        return HttpResponseRedirect('/manage')
    if request.method == 'POST' and 'register' in request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.password = make_password(form.cleaned_data['password'])
            team.save()
            team.backend = 'web.backends.TeamAuthBackend'
            login(request, team)
            request.session['team'] = team.name
            messages.success(request, 'Team {} successfully registered'.format(team.name))
            return HttpResponseRedirect('/')
    elif request.method == 'POST' and 'signin' in request.POST:
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid team name or password')
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
        if request.method == 'POST' and 'submit' in request.POST:
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
                return HttpResponseRedirect('/manage')
        elif request.method == 'POST' and 'delete' in request.POST:
            logout(request)
            request.session['team'] = None
            team.delete()
            messages.success(request, 'Your team has been deleted')
            return HttpResponseRedirect('/')
        else:
            form = ManageTeamForm(instance=team)
    return render(request, 'manage.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def scoreboard(request):
    table = TeamScoreboard(Team.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'scoreboard.html', {'table': table})
