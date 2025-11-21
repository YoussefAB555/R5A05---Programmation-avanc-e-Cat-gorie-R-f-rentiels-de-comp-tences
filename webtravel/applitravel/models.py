from django.db import models
from django.contrib.auth.models import User

class Ville(models.Model):
    IDVille = models.AutoField(primary_key=True)
    NomVille = models.CharField(max_length=80)
    NomPays = models.CharField(max_length=80)
    def __str__(self): return f"{self.NomVille} ({self.NomPays})"

class Voyage(models.Model):
    IDVoyage = models.AutoField(primary_key=True)
    Titre = models.CharField(max_length=120)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='imagesVoyages/', default='imagesVoyages/default.jpg')
    def __str__(self): return f"{self.Titre} - {self.Prix} €"

class Composition(models.Model):
    IDEtape = models.AutoField(primary_key=True)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    nbJours = models.PositiveIntegerField(default=1)
    class Meta:
        unique_together = (('voyage','ville'),)
    def __str__(self): return f"{self.ville} - {self.nbJours} jour(s)"

class Commande(models.Model):
    IDCommande = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande {self.IDCommande} par {self.user.username}"

    @property
    def total(self):
        return sum(item.sous_total for item in self.items.all())

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.voyage.Titre}"

    @property
    def sous_total(self):
        return self.quantite * self.voyage.Prix