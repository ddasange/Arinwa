'''
Created on 21 sept. 2018

@author: djoma
'''

from django.conf.urls import url
from essai1 import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name = 'arinwa/index.html')),
        url(r'^langue/(?P<langue>\w{2})/$', views.choix_langue, name="choix"),
        url(r'^accueil/', views.accueil, name="accueil"),
        url(r'^accueil1/', views.accueil1, name="accueil1"),
        url(r'^about/', views.about, name="about"),
        url(r'^event/', views.evenement, name="even"),
        url(r'^login/', views.login, name = 'connexion'),
        url(r'^register/', views.register, name = "register"),
        url(r'^video/', views.video, name='video'),
        url(r'^documents/(?P<categorie>\d+)/$', views.documents, name = 'documents'),
        url(r'^documents/(?P<categorie>\d+)/(?P<page>\d+)/$', views.documents, name = 'documents'),
        url(r'^documents/downloads/(?P<document>\d+)/$', views.downloads, name = "downloads"),
        url(r'^lois/(?P<pays>\d+)/$', views.lois, name="lois"),
        url(r'^lois/(?P<pays>\d+)/(?P<page>\d+)/$', views.lois, name = "lois"),
        url(r'^lois/downloads/(?P<identifiant>\d+)/$', views.telechargements, name = 'telechargements'),
        #url(r'^documents/recommandations/$', views.recommandations, name="recommandations"),
        #url(r'^documents/jurisprudences/$', views.jurisprudences, name="juriprudences"),
        #url(r'^documents/legislations/', views.legislations, name="legislations"),
        url(r'^actualites/$', views.actualites, name='actualites'),
        url(r'^actualites/(?P<page>\d+)/$', views.actualites, name = "actualites"),
        url(r'^actualite/(?P<identifiant>\d+)/$', views.actualite, name = "actualite"),

        url(r'^docu/', views.document),

        url(r'^my/', views.espace_membre),
        url(r'^deconnexion/', views.deconnexion),
        url(r'^amitie/$', views.amitie),
        url(r'^invite/(?P<id>\d+)/$', views.invitation),
        url(r'^accepte/(?P<id>\d+)/(?P<identifiant>\d+)/$', views.accepte),
        # url(r'^message/<int:id>', views.message),

        url(r'^message/(?P<id>\d+)/$', views.message),
        url(r'^amis/', views.list_ami),
        url(r'^sujet/(?P<id>\d+)/$', views.sujet),
        url(r'^forum/(?P<id>\d+)/$', views.f_message),
        url(r'^membres/', views.membre),
        url(r'^list_invit/', views.liste_invitation),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
