# Generated by Django 4.2.3 on 2023-07-11 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sripe_token',
            new_name='stripe_token',
        ),
    ]
