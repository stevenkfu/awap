import random
import string
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.forms import modelformset_factory
from django_tables2 import RequestConfig

from web.forms import TeamForm, ManageTeamForm, AdminLoginForm
from web.models import Team
from web.tables import TeamScoreboard



chars = string.ascii_lowercase + string.digits
ADMIN_PASS = ''.join((random.choice(chars)) for x in range(16))
print(ADMIN_PASS)

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
    if request.method == 'POST' and 'signin' in request.POST:
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/about')
        else:
            messages.error(request, 'Invalid team name or password')
            return HttpResponseRedirect('/about')
    return render(request, 'about.html')

def scoreboard(request):
    if request.method == 'POST' and 'signin' in request.POST:
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/scoreboard')
        else:
            messages.error(request, 'Invalid team name or password')
            return HttpResponseRedirect('/scoreboard')
    table = TeamScoreboard(Team.objects.all(), order_by='total_score')
    RequestConfig(request).configure(table)
    return render(request, 'scoreboard.html', {'table': table})

def admin_login(request):
    return HttpResponseRedirect('/')
    if request.method == 'POST' and 'signin' in request.POST:
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/admin_login')
        else:
            messages.error(request, 'Invalid team name or password')
            return HttpResponseRedirect('/admin_login')
    elif request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['password'])
            if form.cleaned_data['password'] == ADMIN_PASS:
                request.session['admin'] = True
                return HttpResponseRedirect('/admin')
            else:
                return HttpResponseRedirect('/')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})


def admin(request):
    return HttpResponseRedirect('/')
    if not request.session.get('admin', None):
        return HttpResponseRedirect('/')
    elif request.method == 'POST' and 'signin' in request.POST:
        name = request.POST.get('name', None)
        password = request.POST.get('password', None)
        team = authenticate(name=name, password=password)
        if team is not None:
            login(request, team)
            request.session['team'] = team.name
            return HttpResponseRedirect('/scoreboard')
        else:
            messages.error(request, 'Invalid team name or password')
            return HttpResponseRedirect('/scoreboard')
    else:
        fields = ('name', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'score_6', 'score_7', 'score_8', 'score_9', 'score_10')
        AdminManageTeamForm = modelformset_factory(Team, fields=fields)
        if request.method == 'POST' and 'update' in request.POST:
            formset = AdminManageTeamForm(request.POST)
            if formset.is_valid():
                formset.save()
        elif request.method == 'POST' and 'logout' in request.POST:
            request.session['admin'] = False
            return HttpResponseRedirect('/')
        else:
            formset = AdminManageTeamForm()
        return render(request, 'admin.html', {'formset': formset})
