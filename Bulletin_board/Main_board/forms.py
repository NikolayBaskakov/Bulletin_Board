import random
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from allauth.account.forms import SignupForm
from .models import Post, Response

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category'
        ]
        widgets = {
            'text': SummernoteWidget()
        }
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text'
        ]
        
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if len(text) < 10:
            raise ValidationError("Отклик должен быть не менее 10 символов!")
        return cleaned_data
    
class ResponseApplyForm(forms.Form):
    pass

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request) #TODO
        user.is_active = False
        code = str(random.randint(100000, 999999))
        user.code = make_password(code)
        send_mail(
            subject='Код подтверждения!',
            message=f'Ваш код подтверждения: \n {code}',
            from_email=None,
            recipient_list=[user.email]
        )
        user.save()
        return user