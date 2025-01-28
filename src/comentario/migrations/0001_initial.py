# Generated by Django 5.1.5 on 2025-01-27 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proposta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('commentable_type', models.CharField(max_length=255)),
                ('commentable_id', models.BigIntegerField()),
                ('author_id', models.BigIntegerField()),
                ('body', models.CharField(max_length=10000)),
                ('body_lang', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('analyzed_at', models.DateTimeField(default='2000-01-01 00:00:00.000000')),
                ('sentiment', models.IntegerField(default=-1)),
                ('proposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='proposta.proposta')),
            ],
        ),
    ]