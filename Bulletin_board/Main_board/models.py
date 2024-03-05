from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=254, verbose_name='email address')
    code = models.TextField(default=None, null=True)
    verified = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    edit_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст поста')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=20, null=False, unique=True)
    
    def __str__(self):
        return str(self.slug)
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.slug)])
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
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
    name = models.CharField(choices=TYPES, unique=True)
    
    def __str__(self):
        return self.get_name_display()
    
class Response(models.Model):
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Целевой пост')
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(max_length=20, null=False, unique=True)
    applied = models.BooleanField(default=None, null=True)
    
class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
    )