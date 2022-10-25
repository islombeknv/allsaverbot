from rest_framework.utils import json
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import TelegramUserModel
from .serializers import TelegramRegistrationSerializer, UserModelSerializer

from datetime import datetime


class UserListAPIView(ListAPIView):
    serializer_class = TelegramRegistrationSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if pk:
            return TelegramUserModel.objects.filter(tg_id=pk)

        return TelegramUserModel.objects.all()


class TelegramRegistrationView(CreateAPIView):
    serializer_class = TelegramRegistrationSerializer
    queryset = TelegramUserModel.objects.all()


class ReportUserListAPIView(ListAPIView):
    serializer_class = TelegramRegistrationSerializer
    queryset = TelegramUserModel.objects.all()

    def list(self, request, *args, **kwargs):
        data = {}
        data['total'] = TelegramUserModel.objects.count()
        data['uzb'] = TelegramUserModel.objects.filter(lang='uz').count()
        data['rus'] = TelegramUserModel.objects.filter(lang='ru').count()
        data['eng'] = TelegramUserModel.objects.filter(lang='en').count()
        data['day'] = TelegramUserModel.objects.filter(created_at__day=datetime.today().today().day).count()
        data['month'] = TelegramUserModel.objects.filter(created_at__month=datetime.today().today().month).count()
        data['year'] = TelegramUserModel.objects.filter(created_at__year=datetime.today().today().year).count()
        return HttpResponse(json.dumps(data), content_type="application/json")
