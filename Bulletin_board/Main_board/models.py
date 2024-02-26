from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=25)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
class Category(models.Model):
    TANK = 'TK'
    HEALER = 'HL'
    DAMAGE_DEALER = 'DD'
    TRADER = 'TD'
    GUILDMASTER = 'GM'
    QUESTGIVER = 'QG'
    BLACKSMITH = 'BS'
    TANNER = 'TN'
    POTION_MAKER = 'PM'
    SPELL_MASTER = 'SM'
    TYPES = [
        (TANK, 'Танки'),
        (HEALER, 'Хилы'),
        (DAMAGE_DEALER, 'ДД'),
        (TRADER, 'Торговцы'),
        (GUILDMASTER, 'Гилдмастеры'),
        (QUESTGIVER, 'Квестгиверы'),
        (BLACKSMITH, 'Кузнецы'),
        (TANNER, 'Кожевники'),
        (POTION_MAKER, 'Зельевары'),
        (SPELL_MASTER, 'Мастера Заклинаний')
    ]
    name = models.CharField(choices=TYPES)
    
class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)