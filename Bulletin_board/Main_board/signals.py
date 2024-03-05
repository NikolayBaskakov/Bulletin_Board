import random
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password, check_password
from allauth.account.signals import user_signed_up
from .models import Post, User
response_apply = Signal()
response_create = Signal()
email_confirmed_by_code = Signal()

@receiver(signal=response_create)
def apply_handler(sender, post_obj, **kwargs):
    send_mail(
        subject='Новый отклик!',
        message=f'Вам отправили отклик к посту "{post_obj.title}" !',
        from_email=None,
        recipient_list=[post_obj.author.email,]
    )

@receiver(signal=response_apply)
def apply_handler(sender, response_obj, **kwargs):
    send_mail(
        subject='Отклик принят!',
        message=f'Ваш отклик к посту "{response_obj.post.title}" был принят автором!',
        from_email=None,
        recipient_list=[response_obj.author.email,]
    )
    
@receiver(signal=user_signed_up)
def send_confirm_code(sender, user, **kwargs):
    code = str(random.randint(100000, 999999))
    user.code = make_password(code)
    user.save()
    send_mail(
        subject='Код подтверждения!',
        message=f'Ваш код подтверждения: \n {code}',
        from_email=None,
        recipient_list=[user.email]
    )

@receiver(signal=email_confirmed_by_code)
def add_to_standard_group(sender, user, **kwargs):
    user.code = None
    user.groups.add(Group.objects.get(name="common_users"))
    user.save()
    
@receiver(signal=post_save, sender=Post)
def send_newpost_incategory_msg(sender, instance, created, **kwargs):
    if not created:
        return
    
    emails = User.objects.filter(subscriptions__category=instance.category).exclude(post=instance).values_list('email', flat=True)
    for email in emails:
        send_mail(
            subject=f"В категории {instance.category} опубликован новый пост!",
            message=f"В категории {instance.category}, на которую вы подписаны опубликован новый пост! \nПосмотреть пост: http://127.0.0.1:8000{instance.get_absolute_url()} ",
            from_email=None,
            recipient_list=[email,]
        )