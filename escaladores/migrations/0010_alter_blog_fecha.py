# Generated by Django 4.2.6 on 2023-11-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escaladores', '0009_blog_creador_alter_blog_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
