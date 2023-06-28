from django.contrib import admin

from .models import Trainer,Team,Player,EnemyTeam,TimeTable,Match

admin.site.register(Trainer)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(EnemyTeam)
admin.site.register(TimeTable)
admin.site.register(Match)