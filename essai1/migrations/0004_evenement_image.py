# Generated by Django 2.1.2 on 2018-11-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essai1', '0003_f_sujet_accepter'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='image',
            field=models.ImageField(default=1, upload_to='evenement'),
            preserve_default=False,
        ),
    ]
