from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    name = models.CharField('Primeiro nome', max_length=150, blank=False)
    last_name = models.CharField('Sobrenome', max_length=150, blank=False)
    username = models.CharField('Username', max_length=150, unique=True,
                                validators=[username_validator],
                                error_messages={
                                    'unique': "Nome de usuário já existente",
                                })
    is_staff = models.BooleanField('staff status', default=True)
    email = models.EmailField('e-mail', max_length=150, blank=False)
    about_me = models.TextField('Profile', max_length=500, blank=True)
    profile_pic = models.ImageField('Foto do perfil', upload_to='media', blank=True)


class Game(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor')
    name_game = models.CharField('Nome do jogo', max_length=50)
    release_year = models.DecimalField('Ano de Lançamento', max_digits=4, decimal_places=0)
    text = models.TextField('Resumo do jogo',())
    date_publish = models.DateField('Data de publicação', default=timezone.now)
    game_img = models.ImageField('Foto do Game', upload_to='media', blank=False)

    def publish_game(self):
        self.publish_game = timezone.now()
        self.save()

    def __str__(self):
        return self.name_game
