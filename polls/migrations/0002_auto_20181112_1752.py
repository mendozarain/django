# Generated by Django 2.1 on 2018-11-12 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qestion_text',
            new_name='question_text',
        ),
    ]
