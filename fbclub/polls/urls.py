from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:timetable_id>/', views.detail, name='detail'),
    path("teams/", views.teams, name="teams"),
    path('teams/<int:teams_id>/', views.deteams, name='deteams'),
    path("matchi/", views.matchi, name="matchi"),
    path('matchi/<int:matchi_id>/', views.dematchi, name='dematchi')
]
