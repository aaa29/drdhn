from django.urls import include, path
from rest_framework import routers
from .views import EquipeViewSet, MembreViewSet, ProjectViewSet, AssignmentViewSet, RoleViewSet, PositionViewSet, add


router = routers.DefaultRouter()
router.register('membres', MembreViewSet)
router.register('equipes', EquipeViewSet)
router.register('projects', ProjectViewSet)
router.register('assignments', AssignmentViewSet)
router.register('roles', RoleViewSet)
router.register('position', PositionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('add/', add)
]