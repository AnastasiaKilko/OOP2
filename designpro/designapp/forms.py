from email.policy import default
from enum import unique

from django import forms
from .models import AdvUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email address')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name', 'district')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Username', help_text='Latin letters and hyphen only.',
                               validators=[RegexValidator('^[a-zA-Z-]', message='Your username is wrong. Please, try again.')],
                               error_messages={'unique': 'This username is already taken.'})
    email = forms.EmailField(required=True, label='Email address')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput,
                                help_text='Repeat password')
    last_name = forms.CharField(required=True, label='Last name', widget=forms.TextInput,
                                validators=[RegexValidator('^[а-яА-ЯёЁ-]+\s',
                                                           message='Your last name format is wrong. Please, try again.')])
    first_name = forms.CharField(required=True, label='First name', widget=forms.TextInput,
                                 validators=[RegexValidator('^[а-яА-ЯёЁ-]+\s',
                                                           message='Your first name format is wrong. Please, try again.')])
    middle_name = forms.CharField(required=True, label='Middle name', widget=forms.TextInput,
                                  validators=[RegexValidator('^[а-яА-ЯёЁ-]+\s',
                                                           message='Your middle name format is wrong. Please, try again.')])
    USER_DISTRICT = (
        ('k', 'Кировский'),
        ('l', 'Ленинский'),
        ('o', 'Октябрьский'),
    )
    district = forms.ChoiceField(choices=USER_DISTRICT)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Passwords do not match', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2',
                  'last_name', 'first_name', 'middle_name', 'district', 'send_messages')