from django.db import models

NATIONALITY_CHOICES = [
    ('AF', 'Afegão'),
    ('AL', 'Albanês'),
    ('DZ', 'Argelino'),
    ('AR', 'Argentino'),
    ('AU', 'Australiano'),
    ('BR', 'Brasileiro'),
    ('CA', 'Canadense'),
    ('CN', 'Chinês'),
    ('FR', 'Francês'),
    ('DE', 'Alemão'),
    ('IN', 'Indiano'),
    ('IT', 'Italiano'),
    ('JP', 'Japonês'),
    ('MX', 'Mexicano'),
    ('RU', 'Russo'),
    ('ZA', 'Sul-africano'),
    ('ES', 'Espanhol'),
    ('SE', 'Sueco'),
    ('CH', 'Suíço'),
    ('US', 'Americano'),
]


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    natinality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
    )

    def __str__(self):
        return self.name