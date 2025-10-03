from django.db import models

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