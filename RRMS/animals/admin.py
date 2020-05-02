from django.contrib import admin
from django import forms

from .models import PetStats, IntakeStory, NameAlias, BehavorialHealthIssues
# Register your models here.

admin.site.register(PetStats)
admin.site.register(IntakeStory)
admin.site.register(NameAlias)
admin.site.register(BehavorialHealthIssues)