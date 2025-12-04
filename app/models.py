from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
import requests
import json


# Create your models here.
class DiscordWebhook(models.Model):
    nome = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)

    def enviar_mensagem(self, msg: str, user: AbstractUser):
        print("DENTRO DO WEBHOOK", msg)

        data = {
            "content": msg,
        }
        payload = json.dumps(data)

        headers = {
            "Accept": "Accept: application/json",
            "content-type":	"application/json",
        }

        res = requests.post(self.url, data=payload, headers=headers)

        print("Resultado do coiso: ", res)
        print("Resultado do coiso: ", res.text)

        MsgWebhook.objects.create(
            user = user,
            msg = msg,
            webhook = self
        ).save()
    
    def __str__(self):
        return str(self.nome)

class MsgWebhook(models.Model):
    data = models.DateTimeField(blank=False, default=timezone.localtime)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    webhook = models.ForeignKey(DiscordWebhook, null=False, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255)

