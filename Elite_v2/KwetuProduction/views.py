from django.shortcuts import render, get_object_or_404, redirect
from .models import tproduit
import qrcode as qr



def index(request):
    context= tproduit.objects.all()
    return render(request, 'kwetup/index.html', {'articles':context})

def showArticle(request, produit_id):

    articles = tproduit.objects.all()

    context = {'produit': get_object_or_404(tproduit, pk=produit_id),
               'articles':articles}

    return render(request, 'kwetup/showArticle.html', context)

def profil(request):
    return render(request, 'kwetup/profil.html')

def add(request):

    if request.method == "POST":
        pass
