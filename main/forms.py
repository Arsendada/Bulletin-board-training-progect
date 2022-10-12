from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

from django.contrib.auth.models import User

from .models import *


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput,
                               help_text='Введите пароль повторно')

    class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperRubric.objects.all(), empty_label=None,
        label='Надрубрика', required=True
    )

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}
AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields = '__all__')