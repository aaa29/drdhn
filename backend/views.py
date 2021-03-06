from django.shortcuts import render
from .models import Membre, Equipe, Project, Assignment, Role, Position, Axe, Paxe
from django.contrib.auth.models import User
from .serializers import MembreSerializer, EquipeSerializer, ProjectSerializer, AssignmentSerializer, UserSerializer, RoleSerializer, PositionSerializer, AxeSerializer, PaxeSerializer
from rest_framework.decorators import action, parser_classes, api_view, permission_classes, authentication_classes

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AxeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Axe.objects.all()
    serializer_class = AxeSerializer


class PaxeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Paxe.objects.all()
    serializer_class = PaxeSerializer


class PositionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class MembreViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer

class EquipeViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer



@api_view(['get'])
@permission_classes([AllowAny,])
def add(request, format=None):

    
    with open("temp.txt", "r", encoding="utf8") as f:
        all_ = f.read().split('\n')

        for line in all_:
            axe = Axe(name=line, description=line)
            axe.save()
    

    response = {'userinfo' : 'success'}
    return Response(response, status=status.HTTP_200_OK)
