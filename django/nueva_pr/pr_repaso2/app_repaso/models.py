from django.db import models

class MiCurso(models.Model):
    instructor = models.CharField(max_length=100)
    competencia = models.CharField(max_length=200)
    ambiente = models.CharField(max_length=200)
    aprendiz = models.CharField(max_length=100)
    
    # Nuevos campos añadidos
    duracion = models.CharField(max_length=50, default="40 horas")
    cupos = models.IntegerField(default=30)

    class Meta:
        db_table = 'mi_curso'

    def __str__(self):
        return self.competencia