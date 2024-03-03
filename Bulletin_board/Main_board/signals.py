from django.dispatch import receiver, Signal
from django.core.mail import send_mail
response_apply = Signal()

@receiver(signal=response_apply)
def apply_handler(sender, class_obj, **kwargs):
    send_mail(
        subject='Отклик принят!',
        message=f'Ваш отклик к посту "{class_obj.post.title}" был принят автором!',
        from_email=None,
        recipient_list=[class_obj.author.email,]
    )