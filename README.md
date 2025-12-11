# django-discord webhook
Ferramenta que utiliza uma interface django para interagir com webhooks do Discord.

![](https://github.com/gabriel-ataide-sudo/django-discord-webhook/blob/main/github/image.png)
![](https://github.com/gabriel-ataide-sudo/django-discord-webhook/blob/main/github/image2.png)

Alunos: Gabriel Ataíde de Almeida, Lucas Paulo de Souza Navegante, Pedro Henrique Barbosa Pires da Costa.

## Passo-a-passo para rodar
1. [intale o python](https://www.python.org/downloads/).
2. Crie um venv e instale as dependências do programa:
``` bash
# Linux
python -m venv venv

source ./venv/bin/activate

pip install -r requirements
```
``` powershell
# windows
py -m venv venv

venv/scripts/activate

pip install -r requirements
```
3. Execute o programa:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

4. Interface estará disponível em [http://localhost:8000](http://localhost:8000)
> Login padrão é admin admin

## Adicionando um novo webhook
1. Entrar no seu servidor do Discord, no canal de texto desejado, e abrir suas configurações
   
![](https://github.com/gabriel-ataide-sudo/django-discord-webhook/blob/main/github/image3.png)

2. Abrir o menu de integrações, e então webhooks.
   
![](https://github.com/gabriel-ataide-sudo/django-discord-webhook/blob/main/github/image4.png)

3. Criar um novo webhook para aquele canal.
   
![](https://github.com/gabriel-ataide-sudo/django-discord-webhook/blob/main/github/image5.png)

4. Então basta copiar o nome e url do webhook criado para os campos correspondentes no django e adicioná-lo.
