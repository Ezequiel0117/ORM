from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist


# Función de validación personalizada para el título
def validar_titulo(titulo):
    if 'cobol' in titulo:
        raise ValidationError(f'{titulo} no se vende mucho')
    return titulo

class LibroManager(models.Manager):
    def buscar_por_isbn(self, isbn):
        try:
            buscado = self.get(pk=isbn)
        except ObjectDoesNotExist:
            buscado = f'No existe el libro con ISBN {isbn}'
        finally:
            return buscado
    
    def LibroPorPaginasDjango(self,pagina): 
        from django.core.paginator import Paginator 
        # Recibe los registros a paginas y la cantidad de registros por pagina 
        p = Paginator(Libro.objects.all().order_by('isbn'), 5 ) 
        # y podemos obtener el numero de paginas 
        print(f'Pagina {pagina} / {p.num_pages}') 
        # o los registros de una determinada pagina 
        pag = p.page(pagina) 
        return pag.object_list

# Modelo Editorial
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'libreria_editorial'

# Modelo Libro con valores predeterminados para todos los campos requeridos
class Libro(models.Model):
    isbn = models.CharField(max_length=13, default='0000000000000')  # Valor predeterminado temporal
    titulo = models.CharField(max_length=70, blank=True, validators=[validar_titulo])
    paginas = models.PositiveIntegerField(default=100, db_index=True)
    fecha_publicacion = models.DateField(null=True)
    imagen = models.URLField(max_length=85, null=True)
    desc_corta = models.CharField(max_length=2000, default='Descripción no disponible')
    estatus = models.CharField(max_length=1, default='A')
    categoria = models.CharField(max_length=50, default='General')
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT, default=1)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(titulo='cobol'), name='titulo_no_permitido_chk')
        ]
    
    objects = LibroManager()
    
    def __str__(self):
        return self.titulo 

# Modelo LibroCronica con relación uno a uno con Libro
class LibroCronica(models.Model):
    descripcion_larga = models.TextField(null=True)
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, primary_key=True)

# Modelo Autor con relación muchos a muchos con Libro
class Autor(models.Model):
    nombre = models.CharField(max_length=70)
    libro = models.ManyToManyField(
        Libro, 
        through='AutorCapitulo', 
        related_name='libros_autores', 
        through_fields=('autor', 'libro')
    )
    
    def __str__(self):
        return self.nombre    

# Modelo intermedio AutorCapitulo para extender la relación muchos a muchos entre Autor y Libro
class AutorCapitulo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    numero_capitulos = models.IntegerField(default=1)  # Valor predeterminado para evitar errores
