from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    workers = Worker.objects.all()
    specciality = Speciality.objects.all()
    return render(request, 'home.html',{'workers': workers ,'speciality': specciality} )
def gallery(request):
    galleries = Gallery.objects.select_related('speciality').all()
    specialities = {}
    for gallery in galleries:
        if gallery.speciality not in specialities:
            specialities[gallery.speciality] = []
        specialities[gallery.speciality].append(gallery)


    paginated_specialities = {}
    for speciality, images in specialities.items():
        paginator = Paginator(images, 5)  
        page_number = request.GET.get(f'page_{speciality.id}')  
        try:
            paginated_images = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_images = paginator.page(1)
        except EmptyPage:
            paginated_images = paginator.page(paginator.num_pages)
        
        paginated_specialities[speciality] = paginated_images

    return render(request, 'gallery.html', {'paginated_specialities': paginated_specialities})

def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)  
            return redirect('home')  
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def user_login(request):
       if request.method == 'POST':
           form = LoginForm(request.POST)
           if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(request, username=username, password=password)
               if user is not None:
                   login(request, user)
                   return redirect('home')
               else:
                   return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
       else:
           form = LoginForm()
       return render(request, 'login.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('home')

def record_appointment(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)  
        if form.is_valid():
            record = form.save(commit=False)
            record.client = request.user  
            record.save()
            return redirect('home') 
    else:
        form = RecordForm()  
    return render(request, 'record.html', {'form': form})

def worker(request):
    workers = Worker.objects.all()
    return render(request, {'workers': workers})

def speciality(request):
    speccialities = Speciality.objects.all()
    return render(request,{'speccialities': speccialities})

def success(request):
    return render(request, 'home.html')




