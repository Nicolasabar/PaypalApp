from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from wallet.models import Wallet


class User(AbstractUser):
    email = models.EmailField(_('email add'), unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True)
    #Relacion uno a uno Usuario a Wallet
    wallet = models.OneToOneField(Wallet, on_delete=models.SET_NULL, null=True)
    id_user_stripe  = models.CharField(max_length=255, blank=True)
    
    USERNAME_FIELD = 'email' # de manera default USERNAME_FIELD usa username, al paser el 'email' usara email para iniciar sesion
    REQUIRED_FIELDS = []
