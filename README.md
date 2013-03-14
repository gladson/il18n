Erro ao tentar compilar uma tradução do Django 1.5.

Gettext version:

gettext (GNU gettext-runtime) 0.18.1

Copyright (C) 1995-1997, 2000-2007 Free Software Foundation, Inc.

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Written by Ulrich Drepper.

Rodando sobre Debian Sid com Gnome 3,

    virtualenv==1.7.1.2,
    pip==-1.1-py2.7,
    python 2.7.3.

Menssagem de erro (texto em vermelho) quando é executado 

    "python ../manage.py compilemessages":
    
    processing file django.po in /home/dani/Development/django/env/project/locale/pt_BR/LC_MESSAGES

Para instalar: Clone o repositório (git clone); 

Crie um ambiente virtualenv com Python 2.7.x (virtualenv env); 

Ative seu ambiente virtual Python (source env/bin/activate); 

Instale as depêndencias (pip install -r requeriments.txt); 

Vá para o diretório project (cd project); Execute a compilação (python ../manage.py compilemessages).
