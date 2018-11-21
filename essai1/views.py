from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate
from django.test import Client
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.urls import reverse
from essai1.models import *
from django.core.paginator import Paginator, EmptyPage

"""Diak en action"""
from django.contrib.auth import authenticate, logout, login as dj_login
from .models import *
from django.db.models import Q

# Create your views here.
"""Diak
    prend  
        le
            relais"""

def choix_langue(self, langue):
    activate(langue)
    return redirect(accueil)
    
    

def accueil(request):
    objectif_arinwa = Concernant_arinwa.objects.filter(publier=True).latest('date')
    sliders = Contenu_image.objects.filter(publier = True).order_by('-date')[:3]
    documents = Document.objects.filter(publier = True).order_by('-date')[:6]
    actualites = Actualite.objects.filter(publier = True).order_by('-date')[:6]
    evenements = Evenement.objects.filter(publier = True).order_by('-date')
    categories = Categorie.objects.all()
    liens = Lien.objects.all()
    pays = Pays.objects.all()


    
    
    
    fait = 1;
    slider_list = []
    for slider in sliders:
        if fait == 1 :
            first_slider = slider
            fait += 1
        else:
            slider_list.append(slider)
    
    return render(request, 'arinwa/accueil.html', locals())

def accueil1(request):
    objectif_arinwa = Concernant_arinwa.objects.filter(publier=True).latest('date')
    sliders = Contenu_image.objects.filter(publier = True).order_by('-date')[:3]
    documents = Document.objects.filter(publier = True).order_by('-date')[:6]
    actualites = Actualite.objects.filter(publier = True).order_by('-date')[:6]
    evenements = Evenement.objects.filter(publier = True).order_by('-date')
    categories = Categorie.objects.all()
    liens = Lien.objects.all()
    pays = Pays.objects.all()


    
    
    
    fait = 1;
    slider_list = []
    for slider in sliders:
        if fait == 1 :
            first_slider = slider
            fait += 1
        else:
            slider_list.append(slider)
    
    return render(request, 'arinwa/accueil.html', locals())


def about(request):
    about = Apropos.objects.filter(publier = True).order_by('-date')[:1]
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    
    for apropos in about :
        image = apropos.image.url
        
    
    
    return render(request, 'arinwa/about.html', locals())

def actualites(request, page=1):
    page = int(page)
    country = Pays.objects.all()
    actualites_list = Actualite.objects.filter(publier = True).order_by('-date')
    paginator = Paginator(actualites_list, 2)
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    
    suivant1 = page + 1
    suivant2 = page + 2
    suivant3 = page + 3
    suivant4 = page + 4
    suivant5 = page + 5
    country1 = []
    country2 = []
    count = 0
    for c in country:
        count += 1
        if count <= 4 :
            country1.append(c)
        else:
            country2.append(c)
    
    try :
        actualites = paginator.page(page)
    except EmptyPage :
        actualites = paginator.page(paginator.num_pages)
        
    return render(request, 'arinwa/actualites.html', locals())

def actualite(request, identifiant):
    country = Pays.objects.all()
    new = get_object_or_404(Actualite, pk = identifiant)
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
        
    country1 = []
    country2 = []
    count = 0
    for c in country:
        count += 1
        if count <= 4 :
            country1.append(c)
        else:
            country2.append(c)
    
    return render(request, "arinwa/actualite.html", locals())


def video(request):
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    
    return render(request, 'arinwa/video.html', locals())

def documents(request, categorie, page = 1):
    page = int(page)
    document_actuel = categorie
    documents = Document.objects.filter(categorie_id=categorie, publier=True)
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    categories = Categorie.objects.all()
    paginator = Paginator(documents, 20, 5)
    suivant1 = page + 1
    suivant2 = page + 2
    suivant3 = page + 3
    suivant4 = page + 4
    suivant5 = page + 5
    
    try :
        documents = paginator.page(page)
    except EmptyPage :
        documents = paginator.page(paginator.num_pages)
        
    return render(request, 'arinwa/documents.html', locals())

def downloads(request, document):
    categories = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    downloads = get_object_or_404(Document, pk=document)
    
    return render(request, 'arinwa/downloads.html', locals())

def telechargements(request, identifiant):
    categorie = Categorie.objects.all()
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    downloads = get_object_or_404(Lois, pk = identifiant, publier = True)
    
    return render (request, 'arinwa/telechargement.html', locals())

def lois(request, pays, page=1):
    categories = Categorie.objects.all()
    lois = Lois.objects.filter(pays = pays, publier = True)
    pays = Pays.objects.all()
    liens = Lien.objects.all()
    paginator = Paginator(lois, 20, 5)
    
    suivant1 = page + 1
    suivant2 = page + 2
    suivant3 = page + 3
    suivant4 = page + 4
    suivant5 = page + 5
    
    try :
        documents = paginator.page(page)
    except EmptyPage :
        documents = paginator.page(paginator.num_pages)
    
    return render(request, 'arinwa/lois.html', locals())


"""
def recommandations(request):
    recommandations = Document.objects.filter(categorie = 1, publier = True)
    
    return render(request, 'arinwa/recommandations.html', locals())

def jurisprudences(request):
    jurisprudences = Document.objects.filter(categorie = 2, publier = True)
    
    return render(request, 'arinwa/jurisprudences.html', locals())

def legislations(request):
    legislations = Document.objects.filter(categorie = 3, publier = True)
    
    return render(request, "arinwa/legislations.html", locals())
"""

"""Diak 
    prend 
            le 
                relai"""

def espace_membre(request):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    evenements = Evenement.objects.all()
    try:
        president = EspacePresident.objects.get(id=1)
    except:
        pass
    try:
        secretaire = EspaceSecretaire.objects.get(id=1)
    except:
        pass
    return render(request, 'index.html', locals())

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user :
            membre = Membre.objects.get(user_id = user.id)
            if membre.accepter == 1:
                dj_login(request, user)
                return redirect(espace_membre)
            else:
                message = "Votre demande d'adhésion n'a pas encore été approuvée"
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect"
    return render(request, 'arinwa/login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(login)

def register(request):
    if request.method == "POST":
        nom = request.POST['nom']
        if nom == "":
            msgNom = "Champ requis"
            errorMsgNom = False
        else:
            errorMsgNom = True

        prenoms = request.POST['prenoms']
        if prenoms == "":
            msgPrenoms = "Champ requis"
            errorMsgPrenoms = False
        else:
            errorMsgPrenoms = True

        email = request.POST['email']
        if email == "":
            msgEmail = "Champ requis"
            errorMsgEmail = False
        else:
            errorMsgEmail = True

        password = request.POST['mDP']
        if password == "":
            msgPassword = "Champ requis"
            errorMsgPassword = False
        else:
            errorMsgPassword = True

        passwordC = request.POST['mDPC']
        if passwordC != password:
            msgPasswordC = "Mot de passe different de mot de passe de comfirmation"
            errorMsgPasswordC = False
        else:
            errorMsgPasswordC = True
        boolean = errorMsgPassword and errorMsgEmail and errorMsgPrenoms and errorMsgNom and errorMsgPasswordC
        if boolean:
            user = User.objects.create_user(email, email, password)
            membre = Membre()
            membre.nom = nom
            membre.prenoms = prenoms
            membre.user = user
            membre.save()
            succes = "Enregistrement effectué avec succès"
        else:
            echec = "Enregistrement non effectué"
    return render(request, 'arinwa/register.html', locals())

def invitation(request, id):
    user = request.user
    membre1 = Membre.objects.get(user_id=user.id)
    amis = membre1.amities.all()
    messages = Message.objects.filter(destinateur_id=membre1.id)
    forum = F_forum.objects.all()
    #---------------------------------------------RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR-------------------------------------------------------#
    invitation = Invitation()
    i = Membre.objects.get(id=id)
    invitation.demandeur = membre1
    invitation.recepteur = i
    invitation.save()
    return redirect(membre)

def liste_invitation(request):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    invitations = Invitation.objects.filter(recepteur_id=membre.id)

    return render(request, 'liste_invit.html', locals())

def accepte(request, id, identifiant):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()

    membre_accepte = Membre.objects.get(id=identifiant)
    nouv_amitie = Amitie()
    nouv_amitie.membre1 = membre
    nouv_amitie.membre2 = membre_accepte
    nouv_amitie.save()
    invit = Invitation.objects.get(Q(Q(recepteur_id=membre.id) & Q(demandeur_id=identifiant)))
    invit.delete()
    return redirect(liste_invitation)

def message(request, id):
    user = request.user.id
    membre = Membre.objects.get(user_id=user)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    conversations = Message.objects.filter(Q(Q(expediteur_id=id) & Q(destinateur_id=membre.id) | Q(expediteur_id=membre.id) & Q(destinateur_id=id)))
    # destinateurs = Message.objects.filter(Q(expediteur_id=membre.id) & Q(destinateur_id=id))
    identifiant = id
    if request.method == 'POST':
        message = request.POST['message']

        courrier = Message()
        courrier.destinateur_id = id
        courrier.expediteur_id = membre.id
        courrier.texte = message
        courrier.save()
    return render(request, 'message.html', locals())

def list_ami(request):
    user = request.user.id
    membre = Membre.objects.get(user_id=user)
    amities = membre.amities.all()
    return render(request, 'list_ami.html', locals())


def sujet(request, id):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    forumClick = F_forum.objects.get(id=id)
    sujet_aut = F_sujet.objects.filter(Q(forum_id=id) & Q(accepter=True))
    if request.method == "POST":
        titre = request.POST['sujet']

        s = F_sujet()
        s.sujet_titre = titre
        s.forum = forumClick
        s.membre = membre
        s.save()
    return render(request, 'sujet.html', locals())


def f_message(request, id):
    user = request.user.id
    membre = Membre.objects.get(user_id=user)
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    sujet_message = F_message.objects.filter(sujet_id=id)
    essai = F_sujet.objects.get(id=id)

    if request.method=="POST":
        texte = request.POST['message']

        f_message = F_message()
        f_message.message_texte = texte
        f_message.sujet = essai
        f_message.membre = membre
        f_message.save()

    return render(request, 'forum.html', locals())



def membre(request):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    membres = Membre.objects.all()
    amis = membre.amities.all()
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    invitation = membre.oInvitation.all()
    return render(request, 'membre.html', locals())

def amitie(request):
    user = request.user
    membre = Membre.objects.get(user_id=user.id)
    membres = Membre.objects.all()
    amis = membre.amities.all() 
    messages = Message.objects.filter(destinateur_id=membre.id)
    forum = F_forum.objects.all()
    invitation = membre.oInvitation.all()

    return render(request, 'ami.html', locals())

#_______________________________________________________________________________________________#
def document(request):
    objectif_arinwa = Concernant_arinwa.objects.filter(publier=True).latest('date')
    sliders = Contenu_image.objects.filter(publier = True).order_by('-date')[:3]
    documents = Document.objects.filter(publier = True).order_by('-date')[:6]
    actualites = Actualite.objects.filter(publier = True).order_by('-date')[:6]
    evenements = Evenement.objects.filter(publier = True).order_by('-date')
    categories = Categorie.objects.all()
    liens = Lien.objects.all()
    pays = Pays.objects.all()

    paginator = Paginator(documents, 20, 5)
    page = 1
    suivant1 = page + 1
    suivant2 = page + 2
    suivant3 = page + 3
    suivant4 = page + 4
    suivant5 = page + 5

    return render(request, 'arinwa/documents.html', locals())

def evenement(request):
    evenement = Evenement.objects.all()
    objectif_arinwa = Concernant_arinwa.objects.filter(publier=True).latest('date')
    sliders = Contenu_image.objects.filter(publier = True).order_by('-date')[:3]
    documents = Document.objects.filter(publier = True).order_by('-date')[:6]
    actualites = Actualite.objects.filter(publier = True).order_by('-date')[:6]
    evenements = Evenement.objects.filter(publier = True).order_by('-date')
    categories = Categorie.objects.all()
    liens = Lien.objects.all()
    pays = Pays.objects.all()
    return render(request, 'arinwa/evenement.html', locals())



