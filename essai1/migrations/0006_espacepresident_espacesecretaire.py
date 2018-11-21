# Generated by Django 2.1.2 on 2018-11-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essai1', '0005_auto_20181116_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspacePresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='DG')),
                ('fonction', models.CharField(max_length=100)),
                ('mot_dg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EspaceSecretaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='DG')),
                ('fonction', models.CharField(max_length=100)),
                ('mot_dg', models.TextField()),
            ],
        ),
    ]
