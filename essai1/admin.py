from django.contrib import admin
from django.utils.text import Truncator
from essai1.models import *

# Register your models here.

class EvenementAdmin(admin.ModelAdmin):
    list_display = ('apercu_description', 'date_debut', 'date_fin', 'publier')
    list_filter = ('description', 'date_debut', 'date_fin', 'publier')
    date_hierarchy = 'date_debut'
    ordering = ('date_debut',)
    search_fields = ('description', 'date_debut', 'date_fin', 'publier')
    
    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Renseignez la date de début et de fin de l\'événement', {
            #'classes': ['collapse', ],
            'fields': ('date_debut', 'date_fin', 'image')
        }),
        # Fieldset 2 : contenu de l'article
        ('Donnez la description de l\'événement', {
            'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
           'fields': ('description', 'publier',)
        }),
    )
    
    def apercu_description(self, evenement):
        return Truncator(evenement.description).chars(40, truncate='...')
    
    apercu_description.short_description = "aperçu de la description"
    
    
    
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'apercu_contenu', 'pays', 'publier',)
    list_filter = ('titre', 'date', 'publier')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'date', 'publier', 'contenu')
    
    fieldsets = (
            ('Renseignez le titre et l\'image de l\'actualité', {
                    'fields':('titre', 'image',)
                }),
            ('Donnez le contenu de l\'actualité ', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('contenu', 'pays', 'publier',)
                }),
        )
    
    def apercu_contenu(self, actualite):
        return Truncator(actualite.contenu).chars(40, truncate='...')
    
    apercu_contenu.short_description = "Aperçu du contenu"
    
class AproposAdmin(admin.ModelAdmin):
    list_display = ('date', 'apercu_contenu', 'le_but', 'juri_membre', 'qui_peut_user' , 'publier')
    list_filter = ('date', 'le_but', 'juri_membre', 'qui_peut_user', 'publier')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('date', 'publier', 'contenu')
    
    fieldsets= (
            ('Renseignez le lien de l\'image', {
                    'fields':('image',)
                }),
            ('Donnez le contenu', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('contenu', 'publier', 'le_but', 'juri_membre', 'qui_peut_user')
                }),
        )
    
    def apercu_contenu(self, apropos):
        return Truncator(apropos.contenu).chars(40, truncate='...')
    
    apercu_contenu.short_description = "Aperçu du contenu"
    
class Concernant_arinwaAdmin(admin.ModelAdmin):
    list_display = ('date', 'apercu_contenu', 'publier',)
    list_filter = ('date', 'publier')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('date', 'publier', 'contenu')
    
    fieldsets= (
            ('Donnez le contenu', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('contenu', 'publier',)
                }),
        )
    
    def apercu_contenu(self, concernant_arinwa):
        return Truncator(concernant_arinwa.contenu).chars(80, truncate='...')
    
    apercu_contenu.short_description = "aperçu du contenu"
    
class Contenu_imageAdmin(admin.ModelAdmin):
    list_display = ('date', 'titre', 'description', 'publier',)
    list_filter = ('titre', 'publier')
    search_fields = ('titre', 'publier', 'contenu')
    
    fieldsets= (
            ('Renseignez le titre et une petite description  de l\'image', {
                    'fields':('titre','description',)
                }),
            ('Donnez le lien de l\'image', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('image', 'publier',)
                }),
        )
    
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'categorie', 'pays', 'publier')
    list_filter = ('titre', 'date', 'categorie', 'pays', 'publier')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'date', 'publier', 'categorie', 'pays', 'contenu')
    
    fieldsets= (
            ('Renseignez le titre et l\'image (l\'image est facultative)', {
                    'fields':('titre','image',)
                }),
            ('Donnez le contenu du document ', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('contenu', 'categorie', 'pays', 'publier')
                }),
        )
    
    def contenu(self, document):
        return Truncator(document.contenu).chars(40, truncate='...')
    
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'commentaire', 'date', 'publier')
    list_filter = ('date', 'publier', 'commentaire')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'date', 'publier', 'commentaire')
    
    fieldsets= (
            (' Donnez le lien de la vidéo ', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('video', 'commentaire', 'publier',)
                }),
        )
    
    
    def commentaire(self, video):
        return Truncator(video.commentaire).chars(40, truncate='...')
    
class LoisAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date', 'publier')
    list_filter = ('date', 'publier', 'titre',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'date', 'publier',)
    
    fieldsets= (
            ('Renseignez le titre et le contenu du documment', {
                    'fields':('titre','contenu',)
                }),
            (' Donnez le pays concerné ', {
                    'description': 'Pour publier, veuillez cocher la case "publier" avant d\'enregistrer ! ',
                    'fields':('pays', 'publier')
                }),
        )
    
    def titre(self, lois):
        return Truncator(lois.titre).chars(40, truncate='...')
    
    titre.short_description = "Aperçu du contenu"

admin.site.register(Evenement, EvenementAdmin)
admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(Apropos, AproposAdmin)
admin.site.register(Concernant_arinwa, Concernant_arinwaAdmin)
admin.site.register(Contenu_image, Contenu_imageAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Pays)
admin.site.register(Categorie)
admin.site.register(Lois, LoisAdmin)
"""Mes models """
admin.site.register(Membre)
admin.site.register(F_categorie)
admin.site.register(F_forum)
admin.site.register(F_sujet)
admin.site.register(F_message)
admin.site.register(Message)
admin.site.register(Amitie)
admin.site.register(Invitation)
admin.site.register(EspaceSecretaire)
admin.site.register(EspacePresident)
admin.site.register(Lien)





