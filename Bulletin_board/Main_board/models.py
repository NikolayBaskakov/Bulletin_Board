from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    edit_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст поста')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    
    def __str__(self):
        return str(self.pk)
    
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
    name = models.CharField(choices=TYPES)
    
    def __str__(self):
        return self.get_name_display()
    
class Response(models.Model):
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='id Целевого поста')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')