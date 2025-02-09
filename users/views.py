from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .message import Message
import json

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = Message(
                    "danger", "Credenciales incorrectas", 
                    400, 
                    "https://th.bing.com/th/id/R.cb5be6500c9137186e27bf55a1e04cba?rik=A7JwgQEVk96XZQ&riu=http%3a%2f%2fassets.stickpng.com%2fimages%2f5a0c69ce82e02d31ecb8d013.png&ehk=4h1vU8JBIfwKeHBiCa0TkuBroXnXyvl1bh9ZXnRePrs%3d&risl=&pid=ImgRaw&r=0")
                return render(request, "login.html", {"message":json.dumps(message.to_dict()), 'form': form})
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    message = Message(
        "info", "Se ha cerrado sesión correctamente", 
        200, 
        "https://media1.tenor.com/m/5fuMNcKDKooAAAAC/thumbs-up-okay.gif")
    form = CustomUserLoginForm()  
    return render(request, "login.html", {"message": message.to_dict(), "form": form})
    
@login_required
def home_view(request):
    return render(request, 'home.html')
