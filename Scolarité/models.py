from django.db import models

# Create your models here.

class Faculté(models.Model):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom


class Filière(models.Model):
    nom = models.CharField(max_length=255)
    faculté = models.ForeignKey(Faculté, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} ({self.faculté.nom})"

class Etudiant(models.Model):
    image = models.FileField(upload_to='uploads/',default=None)  # For general files
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    nom_de_famille = models.CharField(max_length=255)
    filière = models.ForeignKey(Filière, on_delete=models.CASCADE)
    dossier = models.FileField(upload_to='uploads/',default=None)  # For general files
    # OR
    # image = models.ImageField(upload_to='uploads/')  
    
    def __str__(self):
            return f"{self.prenom} {self.nom} {self.nom_de_famille}"
