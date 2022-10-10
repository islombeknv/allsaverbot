from rest_framework import serializers

from .models import *


class TelegramRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        exclude = ['tg_id']

