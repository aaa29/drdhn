from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class Equipe(models.Model):
    name = models.CharField(max_length=300)
    Description = models.TextField()
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Position(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()


class Membre(models.Model):
    f_name = models.CharField(max_length=300)
    l_name = models.CharField(max_length=300)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)








class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, blank=True, null=True)
    chef = models.ForeignKey(Membre, on_delete=models.CASCADE, blank=True, null=True)


class Role(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()


class Assignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

