from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class entrada(models.Model):

    class articulosObjetos(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    Option = (
        ('draft','Draft'),
        ('published', 'Published')
    )


    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, default=1)
    titulo = models.CharField(max_length=255)
    resumen = models.CharField(max_length=300)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', null=False,unique=True)
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User,on_delete=models.PROTECT, related_name='blogposts')
    estado = models.CharField(max_length=10,choices=Option, default='draft')
    objects = models.Manager()
    articulosObjetos = articulosObjetos()

    class Meta:
        ordering = ('-published',),

        def __str__(self) -> str:
            return self.titulo

class comentarios(models.Model):
    Entrada = models.ForeignKey(entrada, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=50)
    email = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ("published",),

        def __str__(self) -> str:
            return f"Comentario por: {self.autor}"
