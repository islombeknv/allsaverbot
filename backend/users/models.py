from django.db import models


class TelegramUserModel(models.Model):
    tg_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    lang = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tg_id}'

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'
