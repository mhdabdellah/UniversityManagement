from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Faculté(models.Model):
    nom = models.CharField(_("Nom"), max_length=255)
    
    class Meta:
        verbose_name = _("Faculté")
        verbose_name_plural = _("Facultés")

    def __str__(self):
        return self.nom


class Filière(models.Model):
    nom = models.CharField(_("Nom"), max_length=255)
    faculté = models.ForeignKey(Faculté, on_delete=models.CASCADE, verbose_name=_("Faculté"))
    
    class Meta:
        verbose_name = _("Filière")
        verbose_name_plural = _("Filières")

    def __str__(self):
        return f"{self.nom} ({self.faculté.nom})"


class Etudiant(models.Model):
    image = models.FileField(_("Image"), upload_to='uploads/', default=None)  # For general files
    prenom = models.CharField(_("Prénom"), max_length=255)
    nom = models.CharField(_("Nom"), max_length=255)
    nom_de_famille = models.CharField(_("Nom de famille"), max_length=255)
    filière = models.ForeignKey(Filière, on_delete=models.CASCADE, verbose_name=_("Filière"))
    dossier = models.FileField(_("Dossier"), upload_to='uploads/', default=None)  # For general files
    
    class Meta:
        verbose_name = _("Étudiant")
        verbose_name_plural = _("Étudiants")

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.nom_de_famille}"






# from django.db import models

# # Create your models here.

# class Faculté(models.Model):
#     nom = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.nom


# class Filière(models.Model):
#     nom = models.CharField(max_length=255)
#     faculté = models.ForeignKey(Faculté, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.nom} ({self.faculté.nom})"

# class Etudiant(models.Model):
#     image = models.FileField(upload_to='uploads/',default=None)  # For general files
#     prenom = models.CharField(max_length=255)
#     nom = models.CharField(max_length=255)
#     nom_de_famille = models.CharField(max_length=255)
#     filière = models.ForeignKey(Filière, on_delete=models.CASCADE)
#     dossier = models.FileField(upload_to='uploads/',default=None)  # For general files
#     # OR
#     # image = models.ImageField(upload_to='uploads/')  
    
#     def __str__(self):
#             return f"{self.prenom} {self.nom} {self.nom_de_famille}"
