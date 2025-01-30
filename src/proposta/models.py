from django.db import models

class Proposta(models.Model):
    id = models.BigAutoField(primary_key=True)
    component_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    votes_count = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    title_lang = models.CharField(max_length=25)
    body = models.CharField(max_length=10000)
    body_lang = models.CharField(max_length=25)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title.get("pt-BR", "Título não definido")
