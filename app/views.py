from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.http import HttpRequest
from .models import DiscordWebhook, MsgWebhook
from django.db.models.manager import BaseManager
from typing import cast

# Create your views here.
@login_required(login_url="login")
def index(request: HttpRequest):
    print("Request user:", request.user)
    metodo = request.method

    if metodo == "POST":
        match request.POST.get("action"):
            case "SAIR":
                logout(request)
                return redirect("login")
            
            case "APAGAR_USUARIO":
                id_usuario = request.POST.get("id")
                usuario = User.objects.filter(id=id_usuario)
                usuario.delete()

            case "CRIAR_USUARIO":
                usuario = request.POST.get("user")
                senha = request.POST.get("password")
                if not (usuario == "" or senha == "" or User.objects.filter(username=usuario).count() >= 1 or usuario is None):
                    a = User.objects.create_user(
                        username=usuario,
                        password=senha,
                        email="example@example.com"
                    )
                    a.save()

            case "CRIAR_WEBHOOK":
                nome = request.POST.get("nome")
                url = request.POST.get("url")

                if not (nome == "" or url == ""):
                    DiscordWebhook.objects.create(
                        nome=nome,
                        url=url
                    ).save()
            
            case "APAGAR_WEBHOOK":
                id_usuario = request.POST.get("id")
                usuario = DiscordWebhook.objects.filter(id=id_usuario)
                usuario.delete()
            
            case "ENVIAR_MSG":
                id_webhook = request.POST.get("id")
                msg = request.POST.get("msg")

                webhook = None
                try:
                    webhook = DiscordWebhook.objects.filter(id=id_webhook)
                except Exception as e:
                    print("Erro: ", e)
                    return render(request, "app/index.html", {})
                
                user = request.user
                print("Id do usuário: ", user.id)

                user = User.objects.filter(id=user.id).first()

                wh = webhook.first()
                # print("WH:", wh)
                # print("WH is not None:", wh is not None)
                # print("User: ", user)
                # print("Tipo de User: ", type(user))
                # print("User is User: ", user is User)
                # print("Msg id not none", msg is not None)

                if wh is not None and msg is not None:
                    wh.enviar_mensagem(msg, user)
                else:
                    print("Não bateu as condições")

            case _:
                print("Dados POST recebidos:", request.POST)
    
    contexto = {
        "usuarios": [x for x in User.objects.all()],
        "webhooks": [x for x in DiscordWebhook.objects.all()],
        "mensagens": [x for x in MsgWebhook.objects.all()] 
    }
    return render(request, "app/index.html", contexto)

def logar(request: HttpRequest):
    print("logar")
    metodo = request.method

    if metodo == "POST":
        print("Método POST")
        usuario = request.POST.get("user")
        senha = request.POST.get("password")
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect("index")
        return render(request, "app/login.html", {"erro": "login inválido"})
    else:
        return render(request, "app/login.html", {})

    return render(request, "app/login.html", {"erro": "???"})
