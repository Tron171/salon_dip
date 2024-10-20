from django.urls import path
from myproject import settings
from .views import *
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register_client'),
    path('logout/', LogoutView, name='logout'),
    path('record/', record_appointment, name='record'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'), 
    
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




def custom_404_view(request, exception):
       return render(request, 'myapp/404.html', status=404)

handler404 = custom_404_view