import time
from django import forms
from .models import Speciality, Worker,  Record, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as UserCreationForm
from .models import User  
from captcha.fields import CaptchaField


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'speciality', 'photo']

class CustomUserCreationForm(UserCreationForm):  # регистарция
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'user_name_reg_input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'user_name_reg_input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'user_name_reg_input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'user_name_reg_input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя','class': 'user_name_reg_input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Электронная почта','class': 'user_name_reg_input'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль','class': 'user_name_reg_input'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля','class': 'user_name_reg_input'}),      
        }

class RecordForm(forms.ModelForm):  #форма записи
    class Meta:
        model = Record
        fields = ['worker', 'speciality', 'email', 'message', 'appointment_date', 'appointment_time']
        widgets = {
            'worker': forms.Select(attrs={'placeholder': 'выберете сотрудника', 'class': 'form-control worker-select'}),
            'speciality': forms.Select(attrs={'class': 'form-control speciality-select'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите вашу электронную почту', 'class': 'form-control email-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение (по желанию)', 'class': 'form-control message-textarea', 'rows': 3}),
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control appointment-date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control appointment-time'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['worker'].queryset = Worker.objects.all() 
        self.fields['speciality'].queryset = Speciality.objects.all()  

class LoginForm(forms.Form):
       username = forms.CharField(max_length=150)
       password = forms.CharField(widget=forms.PasswordInput)
       capcha = CaptchaField()

