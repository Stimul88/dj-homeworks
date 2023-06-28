from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Adv
# from advertisements.permissions import IsOwnerOrAdmin
from advertisements.serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    # permission_classes = [IsAuthenticated]

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []


    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         # return [IsAuthenticated()]
    #         permission_classes = [IsAuthenticated]
    #
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return []
    #     # return [permission() for permission in permission_classes]

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #         # обновить, удалить объявление только владелец или администратор
    #     if self.action in ["update", "partial_update", "destroy"]:
    #         return [IsOwnerOrAdmin()]
    #     return []
