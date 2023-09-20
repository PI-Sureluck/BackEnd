from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Site)
admin.site.register(Odds)
admin.site.register(SureBets)
admin.site.register(Event)