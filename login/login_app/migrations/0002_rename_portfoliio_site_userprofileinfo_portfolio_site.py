# Generated by Django 5.0 on 2024-01-18 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfoliio_site',
            new_name='portfolio_site',
        ),
    ]
