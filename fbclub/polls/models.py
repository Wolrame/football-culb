from django.db import models

class Trainer(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birthday = models.DateField()
    workExp = models.IntegerField(default=0)
    salary =  models.IntegerField(default=0)
    photo = models.ImageField(default='' ,upload_to='static/media', height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.firstName

class Team(models.Model):
    name = models.CharField(max_length=20)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birthday = models.DateField()
    position = models.CharField(max_length=20)
    photo = models.ImageField(default='' ,upload_to='static/media', height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.firstName

class EnemyTeam(models.Model):
    name = models.CharField(max_length=20)
    stats = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class TimeTable(models.Model):
    gameDate = models.DateField()
    gamePlace = models.CharField(max_length=20)
    enemyTeam = models.ForeignKey(EnemyTeam,on_delete=models.CASCADE)
    def __str__(self):
        return self.gamePlace

class Match(models.Model):
    matchResult = models.CharField(max_length=3)
    matchStats = models.CharField(max_length=50)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    enemyTeam = models.ForeignKey(EnemyTeam,on_delete=models.CASCADE)
    timetable = models.ForeignKey(TimeTable,on_delete=models.CASCADE)
    def __str__(self):
        return self.team.name