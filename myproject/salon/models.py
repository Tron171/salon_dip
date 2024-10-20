from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm

class Speciality(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='specialities/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Worker(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Имя сотрудника')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name= 'Специальность')
    photo = models.ImageField(upload_to='workers/', verbose_name= 'Фото сотрудника')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.speciality.name}"
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"



class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='salon_user_set',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='salon_user_permissions_set', 
        blank=True,
    )

    def __str__(self):
        return self.username


class Record(models.Model):
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record with  {self.worker} on {self.appointment_date} at {self.appointment_time}"
    
    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"
    

