from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Adv


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Adv
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        list_open = Adv.objects.filter(creator=self.context["request"].user, status="OPEN")
        if len(list_open) >= 10:
            raise ValidationError("Превышен лимит объявлений в статусе OPEN - 10 шт.")

        # TODO: добавьте требуемую валидацию

        return data

    # def validate(self, data):
    #     """Метод для валидации. Вызывается при создании и обновлении."""
    #
    #     # TODO: добавьте требуемую валидацию
    #     if data.get("status", None) == "OPEN":
    #         list_open = Adv.objects.filter(creator=self.context["request"].user, status="OPEN")
    #         if len(list_open) >= 10:
    #             raise ValidationError("Превышен лимит объявлений в статусе OPEN - 10 шт.")
    #
    #     return data