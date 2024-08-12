from django.shortcuts import render , redirect , HttpResponse
from .forms import userlogin , userregister
from django.contrib import messages
from .models import product
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if request.method == "POST" :
        form = userlogin(request , data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username = username , password = password )
            if user is not None :
                login(request , user )
                return redirect('projet:main')
            else :
                for erreur in form.errors.values():
                    messages.error(request , erreur)
        else :
            for erreur in form.errors.values():
                messages.error(request,erreur)
    else : 
        form = userlogin()
    return render(request , 'app1/login.html' , {'form' : form})

def signup_page(request):
    if request.method == "POST":
        form = userregister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet:login')
        else :
            for erreur in form.errors.values():
                messages.error(request , erreur)
    else :
        form = userregister()
    return render(request , 'app1/signup.html',{'form' : form})

def add_product (request):
    if request.method == "POST":
        try :
            print("POST data:", request.POST)
            print("FILES data:", request.FILES)
            title =  request.POST.get('title')
            status = request.POST.get('status')
            description = request.POST.get('description')
            file = request.FILES.get('file')
            produit = product(
             title = title ,
             status = status ,
             description = description,
             file = file)
            produit.save()
            return redirect('projet:main')
        except Exception as e :
            return HttpResponse(f"erreur de type 404 {e}")
    return render(request , 'app1/main.html')
    
@login_required
def logout_page(request):
    logout(request)
    return redirect('projet:login')

def main_page(request):
    print("la page principal est chargé")
    products = product.objects.all()
    return render(request , 'app1/main.html',{'products' : products})

