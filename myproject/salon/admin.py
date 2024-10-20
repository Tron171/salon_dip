from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('new_name', 'speciality_name', 'display_image')
    def new_name(self, obj):
        return obj.name
    new_name.short_description = 'Имя сотрудника'

    def speciality_name(self, obj):
        return obj.speciality.name if obj.speciality else 'Нет специальности'
    speciality_name.short_description = 'Специальность'

    def display_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="width: 100px; height: auto;" />')
        return "-"

    display_image.short_description = 'Фото'

admin.site.register(Worker, WorkerAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'display_speciality')

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />')
        return "-"
    display_image.short_description = 'Изображение'
    def display_speciality(self, obj):
        return obj.speciality.name if obj.speciality else 'Нет специальности'
    display_speciality.short_description = 'Специальность'
admin.site.register(Gallery, GalleryAdmin)

class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('new_name', 'new_price', 'displai_img',)
    def new_name(self, obj):
        return obj.name
    new_name.short_description = 'Специальности'
    def new_price(self, obj):
        return obj.price
    new_price.short_description = 'Цена'
    def displai_img(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="width: 100px; height: auto;" />')
        return "-"
    displai_img.short_description = 'Фото'
admin.site.register(Speciality, SpecialityAdmin)


class RecorderAdmin(admin.ModelAdmin):
    list_display = ('worker_info', 'speciality_info', 'email', 'message_info', 'appointment_date_info', 'appointment_time_info', 'created_at_info') 

    def worker_info(self, obj):
        return obj.worker.name if obj.worker else 'No Worker'
    worker_info.short_description = 'Сотрудник'
    def speciality_info(self, obj):
        return obj.speciality.name if obj.speciality else 'No Speciality'
    speciality_info.short_description = 'Услуга'
    def email_info(self, obj):
        return obj.client.user.email if obj.client and obj.client.user.username else 'No Email'
    email_info.short_description = 'Email'
    def message_info(self, obj):
        return obj.message if obj.message else 'No Message'
    message_info.short_description = 'Сообщение'
    def appointment_date_info(self, obj):
        return obj.appointment_date if obj.appointment_date else 'No Date'
    appointment_date_info.short_description = 'Дата'
    def appointment_time_info(self, obj):
        return obj.appointment_time if obj.appointment_time else 'No Time'
    appointment_time_info.short_description = 'Время'
    def created_at_info(self, obj):
        return obj.created_at if obj.created_at else 'No Date'
    created_at_info.short_description = 'Дата создания'
admin.site.register(Record, RecorderAdmin)


