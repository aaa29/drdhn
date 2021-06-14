from django.contrib import admin
from .models import Membre, Equipe, Project, Assignment

admin.site.register(Membre)
admin.site.register(Equipe)
admin.site.register(Project)
admin.site.register(Assignment)
