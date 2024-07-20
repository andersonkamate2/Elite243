from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout, authenticate
from .models import Client

User = get_user_model()

# Create your views here.
def register(request):

    if request.method == "POST":
        #traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        imgProfil = request.POST.get("email")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        laste_name = request.POST.get("last_name")

        user = User.objects.create_user(username=username,
                                        password=password,
                                        imgProfil=imgProfil,
                                        email=email,
                                        first_name=first_name,
                                        last_name=laste_name)

        login(request, user)
        return redirect('kwetu:index')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('accounts:connexion')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('kwetu:index')
    return render(request, 'accounts/login.html')

def update(request,user_code):

    UserCli = Client.objects.all()

    client = get_object_or_404(Client, pk=user_code)
    if request.method == "POST":
        Client.username = request.POST.get('username')
        Client.email = request.POST.get('email')

        client.save()
        return redirect('kwetu:profil')
    return render(request, 'accounts/update_user.html', {'client':client,
                                                         'clients': UserCli})