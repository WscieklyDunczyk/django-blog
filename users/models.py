from django.db.models import *
from django.contrib.auth.models import User


class Profil(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    rola = CharField(max_length=25)
    image = ImageField(default='default.jpg', upload_to='profilowe')

    def __str__(self):
        return f'{self.user.username}'
