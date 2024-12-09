from django.shortcuts import render, redirect
from .models import Produit, Commande
from django.core.paginator import Paginator


def index(request):
    
    produit_object =Produit.objects.all() 
    
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        produit_object = Produit.objects.filter(title__icontains=item_name)

    paginator = Paginator(produit_object, 8)
    page = request.GET.get('page')
    produit_object = paginator.get_page(page)

    if request.method == "GET":
        title = request.GET.get('recherche')
        if title is not None:
            produit_object = Produit.objects.filter(title__icontains=title)

    return render(request, 'index.html', {'produit_object': produit_object})
    
def details(request, myid):
    produit_object = Produit.objects.get(id=myid)
    return render(request, 'details.html', {'produit_object':produit_object})

def checkout(request):
    if request.method == 'POST':
        item = request.POST['item']
        total = request.POST['total']
        nom = request.POST['nom']
        email = request.POST['email']
        address = request.POST['address']
        ville = request.POST['ville']
        pays = request.POST['pays']
        number = request.POST['number']
        com = Commande(item=item, nom=nom, email=email, address=address, ville=ville, pays=pays, number=number, total=total)
        com.save()
        return redirect('confirmation')
    
    return render(request, 'checkout.html')


def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'confirmation.html', {'name':nom})
