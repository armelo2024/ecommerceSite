from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=225)
    date_sent = models.DateField(auto_now =True)


    class Meta:
        ordering = ['date_sent']
    def __str__(self):
        return self.name    

class Produit(models.Model):
    title = models.CharField(max_length=225)
    price = models.FloatField()
    descri = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_sent = models.DateField(auto_now=True)     
    class Meta:
        ordering = ['date_sent']

    def __str__(self):
        return self.title 


class Commande(models.Model):
    item = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    date_commande = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return self.nom