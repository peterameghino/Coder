# Generated by Django 4.0.5 on 2022-07-21 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Porfolio', '0002_contactos_remove_post_author_remove_post_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tecnologia', models.CharField(max_length=30)),
                ('emisor', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
