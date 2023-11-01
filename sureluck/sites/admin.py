from django.contrib import admin
from .models import *

class SureBetsAdmin(admin.ModelAdmin):
    list_display = ['teamA', 'oddA', 'oddB', 'teamB']
    list_per_page = 10

class OddsAdmin(admin.ModelAdmin):
    list_display = ['odd', 'team', 'site', 'event']
    list_per_page = 10

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'teamA', 'teamB']
    list_per_page = 10

# Register your models here.
admin.site.register(Site)
admin.site.register(Odds, OddsAdmin)
admin.site.register(SureBets,SureBetsAdmin)
admin.site.register(Event,EventAdmin)
