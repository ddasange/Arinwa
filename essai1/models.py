from django.db import models
from django.utils.translation import ugettext_lazy as _

"""Mes 
    modules
        importés"""
from django.contrib.auth.models import User
# Create your models here.

class publication(models.Model):
    publier = models.BooleanField(default=False, verbose_name = _("publier"))
    
    class Meta:
        abstract = True

class autorisation(models.Model):
    accepter = models.BooleanField(default=False, verbose_name = _("Accepter la demande"))
    class Meta:
        abstract = True

class Evenement(publication):
    date_debut = models.DateField(verbose_name=_("date de début"))
    date_fin = models.DateField(verbose_name=_("date de fin"))
    date = models.DateTimeField(auto_now_add = True)
    description = models.TextField()
    image = models.ImageField(upload_to="evenement/")
    
    def __str__(self):
        return "{0}".format(self.date_debut)
    
    class Meta :
        
        ordering = ["date_debut"]
        verbose_name = _("Evénément")
        
class Categorie(models.Model):
    nom = models.CharField(max_length = 100, verbose_name = _("nom") )
    
    class Meta:
        verbose_name = 'catégorie'
        
    def __str__(self):
        return "{0}".format(self.nom)
    
class Pays(models.Model):
    nom = models.CharField(max_length = 50, verbose_name = _("nom"))
    
    def __str__(self):
        return "{0}".format(self.nom)
        
class Document(publication):
    titre = models.CharField(max_length = 255, verbose_name = _("titre"))
    image = models.ImageField(upload_to = "documents/", blank = True, null = True)
    contenu = models.FileField(upload_to="documents_files/")
    date = models.DateTimeField(auto_now_add = True, verbose_name = _("date d'ajout"))
    categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE, verbose_name = _("catégorie"))
    pays = models.ForeignKey("Pays", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return "{0}".format(self.titre)
    
    class Meta:
        ordering = ["date"]

class Lois(publication):
    titre = models.CharField(max_length = 255, verbose_name = _("titre"))
    contenu = models.FileField(upload_to="lois/")
    date = models.DateTimeField(auto_now_add = True, verbose_name = _("date d'ajout"))
    pays = models.ForeignKey("Pays", on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0}".format(self.titre)

class Actualite(publication):
    titre = models.CharField(max_length = 100, verbose_name = _("titre"))
    image = models.ImageField(upload_to = "actualites/", blank = True, null = True)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add = True, verbose_name = _("date d'ajout"))
    pays = models.ForeignKey("Pays", on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0}".format(self.titre)
    
    class Meta:
        ordering = ["date"]
        verbose_name = _("actualité")
        
        
"""class MessageSent(models.Model):
    nom = models.CharField(max_length = 255, verbose_name = -("nom"))
    numero = models.CharField(max_length = 50, vebose_name = _("numéro de téléphone"))
    email= models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True, verbose_name = _("date de reçu"))
    
    def __str__(self):
        return "{0}".format(self.nom)
    
    class Mea:
        verbose_name = _("message reçu")
        plural = _("messages reçus")
        ordering = ["date"]
        """
class Video (publication):
    video = models.URLField(verbose_name=_("lien de la vidéo"))
    commentaire = models.CharField(max_length = 255, blank = True, null = True, verbose_name = _("commentaire"))
    date = models.DateTimeField(auto_now_add = True, verbose_name = _("date d'ajout"))
    
    def __str__(self):
        return "{0}".format(self.video)
    
    class Meta:
        verbose_name = _("vidéo")
        ordering = ["date"]
        
class Apropos(publication):
    image = models.ImageField(upload_to = "propos/")
    contenu = models.TextField(verbose_name = _("contenu"))
    le_but = models.TextField(verbose_name=_("Quel est le but de Arinwa?"))
    juri_membre = models.TextField(verbose_name= _('Combien de juridictions sont membres?'))
    qui_peut_user = models.TextField(verbose_name= _("Qui peut utiliser ARINWA?"))
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return "{0}".format(self.date)
    
    class Meta:
        verbose_name = _(" A propos de nous")
        verbose_name_plural = _("A propos de nous")
        ordering = ["date"]
    
#class Equipe(models.Model):
#    nom = models.CharField(max_length = 255, verbose_name = _("nom"))
#    habitation = models.CharField(max_length = 100, verbose_name = _("lieu d'habitation"))
#    description = models.CharField(max_length = 255)
#    email = models.EmailField()
    
#   def __str__(self):
#       return "{0}".format(self.nom)

class Concernant_arinwa(publication):
    contenu = models.TextField(verbose_name = _("contenu"))
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return "{0}".format(self.date)
    
    class Meta:
        ordering = ["date"]
        verbose_name = _("concernant arinwa")
        verbose_name_plural = _("concernant arinwa")
        
        
class Contenu_image(models.Model):
    titre = models.CharField(max_length = 100, verbose_name = _("titre"))
    description = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = "sliders/")
    publier = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return "{0}".format(self.titre)
    
    class Meta:
        verbose_name = _("image et description")


"""Repris 
        by 
            diakist ☺☺☺"""
class Membre(autorisation):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    date_naiss = models.DateField(null=True)
    email = models.EmailField()
    sexe = models.CharField(max_length=1, null=True)
    profession = models.CharField(max_length=100, null=True)
    avatar = models.ImageField(upload_to='membre')
    auth = models.IntegerField(null = True, primary_key=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #---------------------------------------------ManyToMany--------------------------------------------------------------------#
    oInvitation = models.ManyToManyField('self', through='Invitation', through_fields=('demandeur', 'recepteur'), related_name='invité', symmetrical=False)
    amities = models.ManyToManyField('self', through='Amitie', related_name="amis", symmetrical=False)
    message = models.ManyToManyField('self', through='Message', through_fields=('expediteur', 'destinateur'), related_name="messages", symmetrical=False)

    def __str__(self):
        return "{} {}".format(self.nom , self.prenoms)

class Message(models.Model):
    texte = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    expediteur = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="expediteur")
    destinateur = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="destinateur")

class Invitation(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    demandeur = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="demandeur")
    recepteur = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="recepteur")

class Amitie(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    membre1 = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="membre1")
    membre2 = models.ForeignKey('Membre', on_delete=models.CASCADE, related_name="membre2")


class F_categorie(models.Model):
    cat_nom = models.CharField(max_length=100)
    cat_ordre = models.IntegerField()

class F_forum(models.Model):
    forum_nom = models.CharField(max_length=100)
    forum_desc = models.TextField()
    auth_vu = models.IntegerField(null=True, primary_key=False)
    auth_sujet = models.IntegerField(null=True, primary_key=False)
    auth_message = models.IntegerField(null=True , primary_key=False)
    categorie = models.ForeignKey('F_categorie', on_delete=models.CASCADE)

class F_sujet(autorisation):
    sujet_titre = models.CharField(max_length=100)
    sujet_date_creation = models.DateTimeField(auto_now_add=True)
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)
    forum = models.ForeignKey('F_forum', on_delete=models.CASCADE)

class F_message(models.Model):
    message_texte = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)
    membre = models.ForeignKey('Membre', on_delete=models.CASCADE)
    sujet = models.ForeignKey('F_sujet', on_delete=models.CASCADE)



class EspacePresident(models.Model):
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='DG')
    fonction = models.CharField(max_length=100)
    mot_dg = models.TextField()


class EspaceSecretaire(models.Model):
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='DG')
    fonction = models.CharField(max_length=100)
    mot_dg = models.TextField()






class Lien(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Nom de l'organisation")
    lien = models.URLField(max_length=200, verbose_name="URL du site")

    def __str__(self):
        return self.nom