from django.db import models

class Proposta(models.Model):
    id = models.BigAutoField(primary_key=True)
    component_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    votes_count = models.IntegerField(default=0)
    title = models.JSONField()
    body = models.JSONField()
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title.get("pt-BR", "Título não definido")


class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentable_type = models.CharField(max_length=255)
    commentable_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    body = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    proposta = models.ForeignKey(Proposta, related_name="comentarios", on_delete=models.CASCADE)

    def __str__(self):
        return self.body.get("pt-BR", "Comentário não definido")
