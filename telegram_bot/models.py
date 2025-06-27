from django.db import models

class  TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True, primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"Telegram UserName is {self.username}"

