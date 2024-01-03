from django.contrib import admin


from .models import Faculté, Filière, Etudiant
from django.utils.translation import gettext_lazy as trans

from django.utils.html import format_html

class FilièreInline(admin.TabularInline):
    model = Filière
    extra = 1  # Number of empty forms to display

class EtudiantInline(admin.TabularInline):
    model = Etudiant
    extra = 1

@admin.register(Faculté)
class FacultéAdmin(admin.ModelAdmin):
    inlines = [FilièreInline]

@admin.register(Filière)
class FilièreAdmin(admin.ModelAdmin):
    inlines = [EtudiantInline]
    
# Register your models here.
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    # list_display = ('prenom', 'nom', 'nom_de_famille','filière','image','dossier')
    # list_display = ('display_image','prenom', 'nom', 'nom_de_famille','filière','display_dossier')
    list_display = ('display_image','prenom', 'nom', 'nom_de_famille','filière','dossier')
    
    list_filter = ('prenom', 'nom', 'nom_de_famille','filière')
    search_fields = ('prenom', 'nom', 'nom_de_famille','filière')

    def display_image(self, obj):
        return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
    display_image.short_description = trans("L'image de l'etudiant ")
    # def display_dossier(self, obj):س
    #     return format_html('<iframe src="{}" width="600" height="500" frameborder="0"></iframe>', obj.dossier.url)
    # display_dossier.short_description = " Le dossier de l'etudiant "
    
# admin.site.register(Faculty)
# admin.site.register(Sector)
# admin.site.register(Student)

admin.site.site_title = "Université De Nouakchott"  # This will change the title tag
admin.site.site_header = "Université De Nouakchott"  # This will change the header text
# admin.site.index_title = "Welcome to University Of Nouakchott Admin"  # This will change the title on the admin homepage
