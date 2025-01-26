from django.db import models

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


class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentable_type = models.CharField(max_length=255)
    commentable_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    body = models.CharField(max_length=10000)
    body_lang = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    proposta = models.ForeignKey(Proposta, related_name="comentarios", on_delete=models.CASCADE)
    analyzed_at = models.DateTimeField(default='2000-01-01 00:00:00.000000')
    sentiment = models.IntegerField(default=-1)

    def __str__(self):
        return self.body
