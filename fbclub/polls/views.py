from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.http import Http404
#Для новичка выглядит устрашающе
#Но мы пойдем по пути, которым следует Django.
def index(request):
    latest_Dates_list = TimeTable.objects.order_by('-gameDate')[:20]
    context = {'latest_Dates_list': latest_Dates_list}
    return render(request, 'polls/index.html', context)

def detail(request, timetable_id):
    timetable = get_object_or_404(TimeTable, pk=timetable_id)
    return render(request, 'polls/detail.html', {'TimeTable': timetable})

def teams(request):
    latest_Teams_list = Team.objects.order_by('-name')[:20]
    context = {'latest_Teams_list': latest_Teams_list}
    return render(request, 'polls/teams.html', context)
def deteams(request, teams_id):
    teams = get_object_or_404(Team, pk=teams_id)
    players = Player.objects.order_by('-team')[:20]
    return render(request, 'polls/deteams.html', {'Team': teams,
            'Player': players})

def matchi(request):
    latest_matchi_list = Match.objects.order_by('-team')[:20]
    context = {'latest_matchi_list': latest_matchi_list}
    return render(request, 'polls/matchi.html', context)
def dematchi(request, matchi_id):
    matchi = get_object_or_404(Match, pk=matchi_id)
    return render(request, 'polls/dematchi.html', {'Match': matchi})
