# Generated by Django 2.1.2 on 2018-11-13 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('titre', models.CharField(max_length=100, verbose_name='titre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='actualites/')),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
            ],
            options={
                'verbose_name': 'actualité',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Amitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apropos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('image', models.ImageField(upload_to='propos/')),
                ('contenu', models.TextField(verbose_name='contenu')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': ' A propos de nous',
                'verbose_name_plural': 'A propos de nous',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'catégorie',
            },
        ),
        migrations.CreateModel(
            name='Concernant_arinwa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('contenu', models.TextField(verbose_name='contenu')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'concernant arinwa',
                'verbose_name_plural': 'concernant arinwa',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Contenu_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, verbose_name='titre')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='sliders/')),
                ('publier', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'image et description',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('titre', models.CharField(max_length=255, verbose_name='titre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='documents/')),
                ('contenu', models.FileField(upload_to='documents_files/')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.Categorie', verbose_name='catégorie')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('date_debut', models.DateField(verbose_name='date de début')),
                ('date_fin', models.DateField(verbose_name='date de fin')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Evénément',
                'ordering': ['date_debut'],
            },
        ),
        migrations.CreateModel(
            name='F_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_nom', models.CharField(max_length=100)),
                ('cat_ordre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='F_forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_nom', models.CharField(max_length=100)),
                ('forum_desc', models.TextField()),
                ('auth_vu', models.IntegerField(null=True)),
                ('auth_sujet', models.IntegerField(null=True)),
                ('auth_message', models.IntegerField(null=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.F_categorie')),
            ],
        ),
        migrations.CreateModel(
            name='F_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_texte', models.TextField()),
                ('message_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='F_sujet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet_titre', models.CharField(max_length=100)),
                ('sujet_date_creation', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.F_forum')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('titre', models.CharField(max_length=255, verbose_name='titre')),
                ('contenu', models.FileField(upload_to='lois/')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepter', models.BooleanField(default=False, verbose_name='Accepter la demande')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('date_naiss', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('sexe', models.CharField(max_length=1, null=True)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('avatar', models.ImageField(upload_to='membre')),
                ('auth', models.IntegerField(null=True)),
                ('amities', models.ManyToManyField(related_name='amis', through='essai1.Amitie', to='essai1.Membre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('destinateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinateur', to='essai1.Membre')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expediteur', to='essai1.Membre')),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='nom')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publier', models.BooleanField(default=False, verbose_name='publier')),
                ('video', models.URLField(verbose_name='lien de la vidéo')),
                ('commentaire', models.CharField(blank=True, max_length=255, null=True, verbose_name='commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
            ],
            options={
                'verbose_name': 'vidéo',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='membre',
            name='message',
            field=models.ManyToManyField(related_name='messages', through='essai1.Message', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='membre',
            name='oInvitation',
            field=models.ManyToManyField(related_name='invité', through='essai1.Invitation', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='membre',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lois',
            name='pays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.Pays'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='demandeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandeur', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='recepteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recepteur', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='f_sujet',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='f_message',
            name='sujet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.F_sujet'),
        ),
        migrations.AddField(
            model_name='document',
            name='pays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.Pays'),
        ),
        migrations.AddField(
            model_name='amitie',
            name='membre1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre1', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='amitie',
            name='membre2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membre2', to='essai1.Membre'),
        ),
        migrations.AddField(
            model_name='actualite',
            name='pays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essai1.Pays'),
        ),
    ]
