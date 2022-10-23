from django.db.models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Publiczny(Manager):
    def query_set(self):
        return super(Publiczny, self).query_set().filter(status='publiczny')


class Post(Model):
    STATUS_CHOICES = (
        ('niezatwierdzony', 'niezatwierdzony'),
        ('publiczny', 'publiczny'),
    )

    autor = ForeignKey(User, on_delete=CASCADE)
    tytul = CharField(max_length=100)
    slug = SlugField(null=True, unique=True)
    image = ImageField(null=True, blank=True, upload_to='featured_image')
    tekst = RichTextUploadingField(blank=True, null=True)

    data_dodania = DateTimeField(default=timezone.now)
    data_edytowania = DateTimeField(auto_now=True)

    status = CharField(max_length=20, choices=STATUS_CHOICES, default='niezatwierdzony')

    # domyślny menadżer modelu
    objects = Manager()
    # customowy menadżer modelu
    publiczne = Publiczny()

    def __str__(self):
        return self.tytul

    def get_absolute_url(self):
        return reverse('posty-detail', kwargs={'slug': self.slug})

    # tworzenie sluga przy dodaniu obiektu post
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tytul)
            # tworzenie opisu postu z 50 pierwszych znaków pola tekst
            # self.opis = self.tekst[:50]
        return super().save(*args, **kwargs)


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE)
