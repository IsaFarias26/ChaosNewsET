# Generated by Django 4.2.3 on 2023-07-06 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_news_noticia_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('coemtario', models.TextField()),
                ('estado', models.BooleanField(default=False)),
                ('noticias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.noticia')),
            ],
        ),
    ]