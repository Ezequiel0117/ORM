from .models import *
from django.db.models import (
    Q, F, Value as V,
    Min,
    Max,
    Avg,
    Sum,
    Count,
    CharField,
    Case,
    When
)
from django.db.models.functions import Concat, Left, Length, Replace
from django.db.models import Prefetch

#Ingresar un autor
autor = Autor.objects.create(nombre='Autor desde el ORM')

#Ingresar varios autores
autores = Autor.objects.bulk_create([ Autor(nombre="Autor 1M"), Autor(nombre="Autor 2M"), Autor(nombre="Autor 3M") ])

# INSERT INTO "libreria_autor" ("nombre")
# VALUES ('Autor 1M'), ('Autor 2M'), ('Autor 3M') RETURNING "libreria_autor"."id"

# Execution time: 0.002008s [Database: default]

# In [2]: autores
# Out[2]: [<Autor: Autor 1M>, <Autor: Autor 2M>, <Autor: Autor 3M>]

# Crear un editorial
editorial_1 = Editorial.objects.create(
    nombre='Editorial Ejemplo'
)

# INSERT INTO "libreria_editorial" ("nombre")
# VALUES ('Editorial Ejemplo') RETURNING "libreria_editorial"."id"

# Crear un libro con valores específicos
libro_1 = Libro.objects.create(
    isbn='1234567890123',
    titulo='Introducción a la Programación',
    paginas=250,
    fecha_publicacion='2024-10-27',
    imagen='https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0',
    desc_corta='Un libro básico sobre programación para principiantes.',
    estatus='B',
    categoria='Informática',
    editorial=Editorial.objects.get(id=1)
)

libro_2 = Libro.objects.create(
    isbn='1234567890124',
    titulo='Introducción a la Programación 2',
    paginas=200,
    fecha_publicacion='2024-10-27',
    imagen='https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0',
    desc_corta='Un libro básico sobre programación para intermedios.',
    estatus='B',
    categoria='Informática',
    editorial=Editorial.objects.get(id=1)
)

libro_3 = Libro.objects.create(
    isbn='1234567890126',
    titulo='Programación Orientada a Objetos',
    paginas=150,
    fecha_publicacion='2024-10-27',
    imagen='https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0',
    desc_corta='Un libro básico sobre programación para Avanzados.',
    estatus='B',
    categoria='Informática',
    editorial=Editorial.objects.get(id=1)
)

# Crear un nuevo libro
libro_4 = Libro.objects.create(
    isbn='1234567890127',
    titulo='Estructuras de Datos',
    paginas=350,
    fecha_publicacion='2024-10-28',
    imagen='https://th.bing.com/th/id/R.6a34c19ff7e8dff58da6a43b96caa14f?rik=5gOo6R33I%2BgqQw&pid=ImgRaw&r=0',
    desc_corta='Un libro completo sobre estructuras de datos y algoritmos.',
    estatus='A',
    categoria='Informática',
    editorial=Editorial.objects.get(id=1)  # Asegúrate de que exista un Editorial con id=1
)

# INSERT INTO "libreria_libro" ("isbn", "titulo", "paginas", "fecha_publicacion", "imagen", "desc_corta", "estatus", "categoria", "editorial_id")
# VALUES ('1234567890123', 'Introducción a la Programación', 250, '2024-10-27', 'https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0', 'Un libro básico sobre programación para principiantes.', 'B', 'Informática', 1) RETURNING "libreria_libro"."id"

#Vincular autores con libros

autor_capitulo_1 = AutorCapitulo.objects.create(
    # autor=autor_1,  # Vinculando con el autor existente
    libro=libro_4,
    numero_capitulos=6
)

autor_capitulo_2 = AutorCapitulo.objects.create(
    # autor=autor_1,  # Vinculando al mismo autor existente
    libro=libro_3,
    numero_capitulos=6  # También 6 capítulos para libro_4
)

autor_capitulo_3 = AutorCapitulo.objects.create(
    # autor=autor_1,  # Vinculando al mismo autor existente
    libro=libro_3,
    numero_capitulos=6  # También 6 capítulos para libro_4
)

#Para conocer un unico registro mediante su pk o id

Libro.objects.get(isbn='1234567890123')

# SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."isbn" = '1234567890123'
#  LIMIT 21
 
#  Out[3]: <Libro: Libro object (1)>

autore_presentar = Autor.objects.all()

# <QuerySet [<Autor: Jason R. Weiss>, <Autor: Peter Small>, <Autor: Spencer Salazar>, <Autor: Ahmed Sidky>, <Autor: Jonathan Anstey>, <Autor: Leo S. Hsu>, <Autor: Dmitry Babenko>, <Autor: Brandon Goodin>]>

# Obtener solo el primer resultado 

Libro.objects.all().first()
# Out[3]: <Libro: Introducción a la Programación>

#Obtener el ultimo
Libro.objects.all().last()

# SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  ORDER BY "libreria_libro"."id" DESC
#  LIMIT 1

# Execution time: 0.000000s [Database: default]
# Out[6]: <Libro: Introducción a la Programación 2>

#Objtener cierta cantidad

Libro.objects.all()[:2]

# Out[7]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  LIMIT 2

# Execution time: 0.000000s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>, <Libro: Introducción a la Programación 2>]>


#Obtener un libro que comience con cierto numero
Libro.objects.filter(isbn__startswith='12')

# Out[9]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."isbn" LIKE '12%' ESCAPE '\'
#  LIMIT 21

# Execution time: 0.000325s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>, <Libro: Introducción a la Programación 2>]>

#Que el libro tengas mas de N paginas
Libro.objects.filter(paginas__gt=200)

# Out[10]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" > 200
#  LIMIT 21

# Execution time: 0.000988s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>]>

# Ejemplo de libros que tienen mas de 200 paginas pero cuyo isbn no sea ninguno de estos dos ('1933988592','1884777600') 

Libro.objects.filter(paginas__gt=200).exclude(isbn__in=('1933988592','1884777600'))  

# Out[11]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE ("libreria_libro"."paginas" > 200 AND NOT ("libreria_libro"."isbn" IN ('1933988592', '1884777600')))
#  LIMIT 21

# Execution time: 0.000493s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>]>


#Libro que tiene 200 o mas de 200 paginas
Libro.objects.filter(paginas__gte=200) 

# Out[12]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" >= 200
#  LIMIT 21

# Execution time: 0.000925s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>, <Libro: Introducción a la Programación 2>]>


#  Seleccionar las columnas a mostrar 
# Ejemplo de una consulta de los libros que tienen 200 o mas paginas, pero solo muestra las columnas isbn y paginas

Libro.objects.filter(paginas__gte=200).values('isbn','paginas')
# Out[1]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."paginas"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" >= 200
#  LIMIT 21

# Execution time: 0.001379s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'paginas': 250}, {'isbn': '1234567890124', 'paginas': 200}]>


# Consultas por menor que Ejemplo de los libros que tienen menos de 200 paginas

Libro.objects.filter(paginas__lt=200)

# Out[3]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" < 200
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [<Libro: Programación Orientada a Objetos>]>

# 3.3.15 Contar COUNT
# Contar los libros que tienen menos de 200 páginas
num_libros_menos_200_paginas = Libro.objects.filter(paginas__lt=200).count()

# SELECT COUNT(*) AS "__count"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" < 200

# Execution time: 0.000000s [Database: default]

# In [12]: num_libros_menos_200_paginas
# Out[12]: 1

# 3.3.16 OR (forma larga)
# Consulta de los libros con 200 páginas o con 300 páginas
consulta1 = Libro.objects.filter(paginas=200)

# Out[6]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" = 200
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación 2>]>

consulta2 = Libro.objects.filter(paginas=300)

# Out[8]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" = 300
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet []>

libros_200_300_paginas = (consulta1 | consulta2).values('isbn', 'paginas')

# In [10]: libros_200_300_paginas
# Out[10]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."paginas"
#   FROM "libreria_libro"
#  WHERE ("libreria_libro"."paginas" = 200 OR "libreria_libro"."paginas" = 300)
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890124', 'paginas': 200}]>

# 3.3.17 Consultar por año de una fecha
# Consulta que muestra los libros cuya fecha de publicación es 2012
libros_publicados_2024 = Libro.objects.filter(fecha_publicacion__year=2024).values('isbn', 'fecha_publicacion')

# Out[14]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."fecha_publicacion"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."fecha_publicacion" BETWEEN '2024-01-01' AND '2024-12-31'
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'fecha_publicacion': datetime.date(2024, 10, 27)}, {'isbn': '1234567890124', 'fecha_publicacion': datetime.date(2024, 10, 27)}, {'isbn': '1234567890126', 'fecha_publicacion': datetime.date(2024, 10, 27)}]>

# 3.3.18 Filtrar usando expresiones regulares
# Consultar los libros cuyo ISBN comienza con un 19 seguido de 8 dígitos
libros_isbn_12 = Libro.objects.filter(isbn__regex=r'12\d{8}$').values('isbn')

#No hay 

# Out[16]: SELECT "libreria_libro"."isbn"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."isbn" REGEXP '12\d{8}$'
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet []>

# 3.3.19 UNION
# Unir en una consulta el nombre de los Autores que contienen 'hill' con las Editoriales cuyo nombre también contiene 'hill'
a1 = Autor.objects.filter(nombre__contains='hill').values('nombre')
e1 = Editorial.objects.filter(nombre__contains='hill').values('nombre')
autores_editoriales_hill = a1.union(e1)

# 3.3.20 El segundo libro con más páginas
# Obtener el segundo libro con más páginas
primer_libro_mas_paginas = Libro.objects.values('isbn', 'paginas').order_by('-paginas')[1]

# In [17]: segundo_libro_mas_paginas = Libro.objects.values('isbn', 'paginas').order_by('-paginas')[1]
#     ...:
# SELECT "libreria_libro"."isbn",
#        "libreria_libro"."paginas"
#   FROM "libreria_libro"
#  ORDER BY "libreria_libro"."paginas" DESC
#  LIMIT 1
# OFFSET 1

# Execution time: 0.000000s [Database: default]

# In [18]: primer_libro_mas_paginas
# Out[18]: {'isbn': '1234567890124', 'paginas': 200}

# 3.3.21 El cuarto y quinto libro con más páginas
# Obtener el cuarto y quinto libro con más páginas
segundo_tercer_libro_mas_paginas = Libro.objects.values('isbn', 'paginas').order_by('-paginas')[1:2]

# Out[20]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."paginas"
#   FROM "libreria_libro"
#  ORDER BY "libreria_libro"."paginas" DESC
#  LIMIT 1
# OFFSET 1

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890124', 'paginas': 200}]>

# Paginando a mano  
 
# No es una buena idea mostrar todos los registros en una consulta, es por eso que una solución es dividir los 
# registros en paginas de un cierto numero de registros, una forma de hacer esto es crear una función como la 
# siguiente en la que las paginas son 5 registros aunque la ultima puede tener 5 o menos registros.

Libro.objects.LibroPorPaginas(1)

# Pagina 1 / 1
# Out[2]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  ORDER BY "libreria_libro"."isbn" ASC
#  LIMIT 3

# Execution time: 0.000000s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>, <Libro: Introducción a la Programación 2>, <Libro: Programación Orientada a Objetos>]>

#Escanear toda las tablas
Libro.objects.filter(paginas__gte=200).explain()

# EXPLAIN QUERY PLAN SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" >= 200

# Execution time: 0.000000s [Database: default]
# Out[5]: '2 0 0 SCAN libreria_libro'

# MIN 
# Calcular cual es el numero minimo de paginas que puede tener un libro, en esta consulta no tomamos en cuenta 
# los libros que no se especifico su numero de paginas por lo cual es 0 y este seria el mínimo numero de paginas.

Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))

# In [6]: Libro.objects.filter(paginas__gt=0).aggregate(Min('paginas'))
#    ...:
# SELECT MIN("libreria_libro"."paginas") AS "paginas__min"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" > 0

# Execution time: 0.000000s [Database: default]
# Out[6]: {'paginas__min': 150}

# MAX 
# Calcular cual es el numero máximo de paginas que puede tener un libro, aquí no necesitamos filtrar, este seria el 
# máximo numero de paginas. 

Libro.objects.aggregate(Max('paginas'))

# In [7]: Libro.objects.aggregate(Max('paginas'))
#    ...:
# SELECT MAX("libreria_libro"."paginas") AS "paginas__max"
#   FROM "libreria_libro"

# Execution time: 0.000000s [Database: default]
# Out[7]: {'paginas__max': 250}

# AVG 
# Calcular cual es el numero medio de paginas que puede tener un libro, en esta consulta no tomamos en cuenta 
# los libros que no se especifico su numero de paginas para así solo considerar los libros con paginas.
Libro.objects.filter(paginas__gt=0).aggregate(Avg('paginas'))

# SELECT AVG("libreria_libro"."paginas") AS "paginas__avg"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" > 0

# Execution time: 0.000000s [Database: default]
# Out[8]: {'paginas__avg': 200.0}

# SUM 
# Sumar el total de paginas de todos los libros que tenemos de Informatica

Libro.objects.filter(categoria__icontains='Informática').aggregate(Sum('paginas'))

# SELECT SUM("libreria_libro"."paginas") AS "paginas__sum"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."categoria" LIKE '%Informática%' ESCAPE '\'

# Execution time: 0.000000s [Database: default]
# Out[9]: {'paginas__sum': 600}

# GROUP BY  
# Para poder agrupar nuestros datos usamos el método annotate y dentro de el podemos contar o usar cualquiera de los 
# métodos de agregación que vimos antes, a continuación te muestro algunos ejemplo de agrupado. 
# 1. Agrupar los libros que son de Python por categoría y contar cuantos libros de cada categoría hay. 

Libro.objects.filter(categoria__contains='Informática').values('categoria').annotate(NumeroLibros=Count('*'))

# Out[10]: SELECT "libreria_libro"."categoria",
#        COUNT(*) AS "NumeroLibros"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."categoria" LIKE '%Informática%' ESCAPE '\'
#  GROUP BY "libreria_libro"."categoria"
#  LIMIT 21

# Execution time: 0.001020s [Database: default]
# <QuerySet [{'categoria': 'Informática', 'NumeroLibros': 3}]>

# Agrupar los libros que son de Informática por categoría y por el nombre de la editorial y contar cuantos libros hay, a 
# diferencia del ejemplo anterior en este ejemplo se involucran dos modelos Libro y Editorial, por lo que estamos 
# hablando también de una union. 

Libro.objects.filter(categoria__icontains='Informática').values('categoria','editorial__nombre').annotate(NumeroLibros=Count('*'))

# Out[11]: SELECT "libreria_libro"."categoria",
#        "libreria_editorial"."nombre",
#        COUNT(*) AS "NumeroLibros"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_editorial"
#     ON ("libreria_libro"."editorial_id" = "libreria_editorial"."id")
#  WHERE "libreria_libro"."categoria" LIKE '%Informática%' ESCAPE '\'
#  GROUP BY "libreria_libro"."categoria",
#           "libreria_editorial"."nombre"
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'categoria': 'Informática', 'editorial__nombre': 'Editorial Ejemplo', 'NumeroLibros': 3}]>

# HAVING (Filtrar agrupados)  
# Para poder filtrar lo que agrupamos utilizamos filter solo que ahora utilizaremos alguna de las columnas que 
# especificamos dentro de annotate, en este ejemplo agrupamos los libros por fecha_publicacion y filtramos solo 
# las tengan mas de N libros publicados en esa fecha. 

#En este caso solo le pongo 1 porque se han publicado en la fecha que seria 2024, si fuera otra seria 5 que se han publicado en otra fecha
Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=1)

# Out[13]: SELECT "libreria_libro"."fecha_publicacion",
#        COUNT("libreria_libro"."fecha_publicacion") AS "cant_fec_pub"
#   FROM "libreria_libro"
#  GROUP BY "libreria_libro"."fecha_publicacion"
# HAVING COUNT("libreria_libro"."fecha_publicacion") >= 1
#  LIMIT 21

# Execution time: 0.001004s [Database: default]
# <QuerySet [{'fecha_publicacion': datetime.date(2024, 10, 27), 'cant_fec_pub': 3}]>

# Si quisiéramos obtener el detalle de los libros de la consulta anterior podemos hacer lo siguiente

# Consulta para obtener las fechas con una o más publicaciones
consulta_fechas =Libro.objects.values('fecha_publicacion').annotate(cant_fec_pub=Count('fecha_publicacion')).filter(cant_fec_pub__gte=1).values_list('fecha_publicacion') 

# Consulta para obtener el detalle de los libros que cumplen la condición anterior
libros_detalle = Libro.objects.filter(fecha_publicacion__in=consulta_fechas).values('isbn')


# Out[16]: SELECT "libreria_libro"."isbn"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."fecha_publicacion" IN (
#         SELECT U0."fecha_publicacion"
#           FROM "libreria_libro" U0
#          GROUP BY U0."fecha_publicacion"
#         HAVING COUNT(U0."fecha_publicacion") >= 1
#        )
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890123'}, {'isbn': '1234567890124'}, {'isbn': '1234567890126'}]>


# DISTINCT  
# Devolver valores únicos de una para evitar ver valores duplicados, en este ejemplo usamos distinct sobre 
# paginas ya que muchos libros tienen 0 paginas. 

Libro.objects.values('paginas').filter(paginas__lt=200).distinct() 

# Out[17]: SELECT DISTINCT "libreria_libro"."paginas"
#   FROM "libreria_libro"
#  WHERE "libreria_libro"."paginas" < 200
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'paginas': 150}]>

# Queremos que nuestra desc_corta solo muestre los primeros 15 caracteres 

Libro.objects.annotate(desc_resumida=Left('desc_corta', 15)).values('isbn', 'desc_resumida')

# Out[3]: SELECT "libreria_libro"."isbn",
#        SUBSTR("libreria_libro"."desc_corta", 1, 15) AS "desc_resumida"
#   FROM "libreria_libro"
#  LIMIT 21

# Execution time: 0.001036s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'desc_resumida': 'Un libro básico'}, {'isbn': '1234567890124', 'desc_resumida': 'Un libro básico'}, {'isbn': '1234567890126', 'desc_resumida': 'Un libro básico'}]>

# Concat y Value
# Queremos concatenar tres puntos (…) al fina de los valores de nuestra desc_resumida, para poder concatenar 
# usamos la función Concat y para especificar la cadena a concatenar usamos Value.

Libro.objects.annotate(desc_resumida=Concat(Left('desc_corta',15),V('...'))).values('isbn','desc_resumida')

# Out[5]: SELECT "libreria_libro"."isbn",
#        (COALESCE(SUBSTR("libreria_libro"."desc_corta", 1, 15), '') || COALESCE('...', '')) AS "desc_resumida"
#   FROM "libreria_libro"
#  LIMIT 21

# Execution time: 0.001064s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'desc_resumida': 'Un libro básico...'}, {'isbn': '1234567890124', 'desc_resumida': 'Un libro básico...'}, {'isbn': '1234567890126', 'desc_resumida': 'Un libro básico...'}]>


# Case  
 
# En el ejemplo anterior le pusimos los tres puntos (…) a todas las filas, en este ejemplo solo se los pondremos a 
# las cadenas cuya longitud sea mayor de 15.

Libro.objects.annotate(longitud = Length('desc_corta')).annotate( 
       desc_resumida = Case( 
                 When(longitud__gt=50, 
     then = Concat(Left('desc_corta',15), V('...'))) 
    , 
                    default=('desc_corta'), 
                    output_field=CharField(), 
                  )).values('isbn','desc_resumida','longitud') 

# Out[9]: SELECT "libreria_libro"."isbn",
#        CASE WHEN LENGTH("libreria_libro"."desc_corta") > 50 THEN (COALESCE(SUBSTR("libreria_libro"."desc_corta", 1, 15), '') || COALESCE('...', ''))
#             ELSE "libreria_libro"."desc_corta"
#              END AS "desc_resumida",
#        LENGTH("libreria_libro"."desc_corta") AS "longitud"
#   FROM "libreria_libro"
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'desc_resumida': 'Un libro básico...', 'longitud': 54}, {'isbn': '1234567890124', 'desc_resumida': 'Un libro básico...', 'longitud': 52}, {'isbn': '1234567890126', 'desc_resumida': 'Un libro básico sobre programación para Avanzados.', 'longitud': 50}]>

# Comparar columnas del mismo modelo (F)  
# Queremos saber que libros tienen un titulo igual a su desc_corta dentro de sus primeros 50 caracteres, para 
# especificar que lo que va a comparar es una columna del modelo y no una cadena de texto usamos 
# F(nombre_columna)

Libro.objects.annotate(tit50= Left('titulo',50), desc50= Left('desc_corta',50)).filter(tit50 = F('desc50')).values('isbn','tit50','desc50') 

#EN este aso no hay ninguo

# Out[10]: SELECT "libreria_libro"."isbn",
#        SUBSTR("libreria_libro"."titulo", 1, 50) AS "tit50",
#        SUBSTR("libreria_libro"."desc_corta", 1, 50) AS "desc50"
#   FROM "libreria_libro"
#  WHERE SUBSTR("libreria_libro"."titulo", 1, 50) = (SUBSTR("libreria_libro"."desc_corta", 1, 50))
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet []>

# Replace 
  
# Queremos quitarle las comillas a los nombres de nuestra categoría y remplazarlas por un *

Libro.objects.annotate(categoria_sin_comillas=Replace('categoria', V('"'), V('*'))).values('isbn', 'categoria', 'categoria_sin_comillas')

# Out[14]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."categoria",
#        REPLACE("libreria_libro"."categoria", '"', '*') AS "categoria_sin_comillas"
#   FROM "libreria_libro"
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'categoria': 'Informática', 'categoria_sin_comillas': 'Informática'}, {'isbn': '1234567890124', 'categoria': 'Informática', 'categoria_sin_comillas': 'Informática'}, {'isbn': '1234567890126', 'categoria': 'Informática', 'categoria_sin_comillas': 'Informática'}]>

# Recuerda que no estamos afectando la base de datos solo estamos mostrando los datos, si quisieras afectar la 
# base de datos y cambiar las comillas por * tendrías que hacer lo siguiente:

Libro.objects.filter(categoria='[]').update(categoria = Replace('categoria', V('"'),V('*')))

# Consultas avanzadas 
# 3.6.1 OR mejorado (usando Q)  
# Ya habíamos visto una forma larga de realizar un  OR (forma larga) vamos a ver una forma mas corta de poder 
# utilizarlo. 
# Para poder hacer esto utilizamos el operador Q(consulta) después podemos aplicar el OR y seguir haciendo 
# condiciones. 
# En este ejemplo queremos las categorías que sean sobre Python o Java o net y que no tengan paginas igual a 0 

Libro.objects.filter((Q(categoria__contains='python') | Q(categoria__contains='java') | Q(categoria__contains='net')) & ~Q(paginas=0)) 

#En este caso no tenemos ninguno

# Out[15]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  WHERE (("libreria_libro"."categoria" LIKE '%python%' ESCAPE '\' OR "libreria_libro"."categoria" LIKE '%java%' ESCAPE '\' OR "libreria_libro"."categoria" LIKE
#  '%net%' ESCAPE '\') AND NOT ("libreria_libro"."paginas" = 0))
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet []>


# LEFT JOIN (en relaciones 1 a 1)   
# Queremos hacer una consulta entre el modelo Libro y LibroCronica, nos interesa saber que libros no tienen 
# crónica, recordemos como esta nuestra relación 1 a 1.

Libro.objects.filter(librocronica__descripcion_larga__isnull=True).values('isbn','titulo','librocronica__descripcion_larga') 

# Out[16]: SELECT "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_librocronica"."descripcion_larga"
#   FROM "libreria_libro"
#   LEFT OUTER JOIN "libreria_librocronica"
#     ON ("libreria_libro"."id" = "libreria_librocronica"."libro_id")
#  WHERE "libreria_librocronica"."descripcion_larga" IS NULL
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# <QuerySet [{'isbn': '1234567890123', 'titulo': 'Introducción a la Programación', 'librocronica__descripcion_larga': None}, {'isbn': '1234567890124', 'titulo': 'Introducción a la Programación 2', 'librocronica__descripcion_larga': None}, {'isbn': '1234567890126', 'titulo': 'Programación Orientada a Objetos', 'librocronica__descripcion_larga': None}]>

# LEFT JOIN (usando select_related relaciones 1 a 1)  
# Existe otra forma de hacer la relacion uno a uno de Libro y LibroCronica y es usando select_related(modelo_relacion). 

Libro.objects.select_related('librocronica').filter(categoria__contains='Informática')

# Out[17]: SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id",
#        "libreria_librocronica"."descripcion_larga",
#        "libreria_librocronica"."libro_id"
#   FROM "libreria_libro"
#   LEFT OUTER JOIN "libreria_librocronica"
#     ON ("libreria_libro"."id" = "libreria_librocronica"."libro_id")
#  WHERE "libreria_libro"."categoria" LIKE '%Informática%' ESCAPE '\'
#  LIMIT 21

# Execution time: 0.001006s [Database: default]
# <QuerySet [<Libro: Introducción a la Programación>, <Libro: Introducción a la Programación 2>, <Libro: Programación Orientada a Objetos>]>

# Beneficios de usar select_related en relaciones 1 a 1 
 
# En el ejemplo anterior hicimos las consultas desde el modelo Libro, que pasaría si lo hiciéramos ahora desde el 
# modelo, vamos a consultar primero nuestro modelo LibroCronica.

LibroCronica.objects.all()[:3]

#No tenemos nada en libro cronica

# Out[18]: SELECT "libreria_librocronica"."descripcion_larga",
#        "libreria_librocronica"."libro_id"
#   FROM "libreria_librocronica"
#  LIMIT 3

# Execution time: 0.000000s [Database: default]
# <QuerySet []>

# Crear una relación con LibroCronica con el libro 4
libro_cronica_1 = LibroCronica.objects.create(
    descripcion_larga='Este libro profundiza en las estructuras de datos más utilizadas y su implementación en diferentes lenguajes de programación.',
    libro=libro_4  # Relaciona con libro_4
)

libro_cronica_2 = LibroCronica.objects.create(
    descripcion_larga='Este libro profundiza en las estructuras de datos más utilizada.',
    libro=libro_3  # Relaciona con libro_3
)
#Ya tenemos 1 libro con cronica

# Out[23]: SELECT "libreria_librocronica"."descripcion_larga",
#        "libreria_librocronica"."libro_id"
#   FROM "libreria_librocronica"
#  LIMIT 3

# Execution time: 0.000000s [Database: default]
# <QuerySet [<LibroCronica: LibroCronica object (4)>]>

# Como puedes ver cuando hacemos la consulta sobre el que se le especifico la relación UNO A UNO, el ORM realiza la 
# consulta primero sobre este modelo para obtener los ids en este caso los isbn después realiza una consulta por cada isbn 
# sobre el modelo al que esta relacionado, en este caso solo fueron 3 registros, como podemos ver este tipo de consultas 
# no es optima si aumentara el numero de registros que estamos consultando 
# Vamos a ver que pasa si utilizamos select_related

LibroCronica.objects.select_related('libro').all()[:3] 

# Out[24]: SELECT "libreria_librocronica"."descripcion_larga",
#        "libreria_librocronica"."libro_id",
#        "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_librocronica"
#  INNER JOIN "libreria_libro"
#     ON ("libreria_librocronica"."libro_id" = "libreria_libro"."id")
#  LIMIT 3

# Execution time: 0.000000s [Database: default]
# <QuerySet [<LibroCronica: LibroCronica object (4)>]>


#En una sola sentencia

# Beneficios de usar select_related en relaciones 1 a muchos  
# Vamos a realizar la consulta anterior pero ahora agregándole select_related especificándole que la relación es 
# sobre el modelo editorial 


categorias = Libro.objects.all().select_related('editorial').filter(categoria__icontains='Informática')
 
# for libro in categorias: 
#     print(libro.editorial.nombre) 
    
#     SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id",
#        "libreria_editorial"."id",
#        "libreria_editorial"."nombre"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_editorial"
#     ON ("libreria_libro"."editorial_id" = "libreria_editorial"."id")
#  WHERE "libreria_libro"."categoria" LIKE '%Informática%' ESCAPE '\'

# Execution time: 0.001000s [Database: default]
# Editorial Ejemplo
# Editorial Ejemplo
# Editorial Ejemplo
# Editorial Ejemplo

#Sin for :

# ¿Y si no quiero utilizar un for para esto? 
# Pues: 

# No se tu pero yo prefiero mis consultas en una sola sentencia SQL. 

consulta = Libro.objects.all().select_related('editorial').filter(categoria__icontains='Informática') 
dic_libros = dict(consulta.values_list('isbn','editorial__nombre')) 
print(dic_libros)

# Consultas de relación muchos a muchos 
# Para realizar las consultas en una relación muchos a muchos es importante saber cual es el modelo que tiene 
# especificada la relación, en los ejemplo que veremos la relación esta en el modelo Autor MUCHOS A MUCHOS. 
# La Consulta en la relación BASICA  de nuestro ejemplo se especifico en el modelo Autor

# Forma optima usando prefetch_related 
# Vamos a realizar la misma consulta anterior pero ahora usaremos el método prefetch_related para especificarle que 
# Autor tiene una relación con libros, y como veremos ahora solo realizara 2 consultas no importa el numero de autores 
# que consultemos. 

# Consulta de autores con ID 1
autores = Autor.objects.filter(pk__in=(1,))  # Usar una tupla con un solo elemento

# Iterar sobre los autores encontrados
for autor in autores:
    print(f'Autor: {autor.nombre}')  # Imprimir el nombre del autor
    print('Libros escritos:')
    
    # Iterar sobre los libros escritos por el autor
    for libro in autor.libro.all():
        print(libro.titulo)  # Imprimir el título de cada libro
        
# Execution time: 0.000000s [Database: default]
# Autor: Jason R. Weiss
# Libros escritos:
# SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_autorcapitulo"
#     ON ("libreria_libro"."id" = "libreria_autorcapitulo"."libro_id")
#  WHERE "libreria_autorcapitulo"."autor_id" = 1

# Execution time: 0.000000s [Database: default]
# Estructuras de Datos
# Estructuras de Datos
# Programación Orientada a Objetos


# Consultas muchos a muchos profundas (forma viable) 
# Vamos a realizar la misma consulta que en el ejemplo anterior solo que esta vez en el prefetch_related le indicaremos 
# que también existe una relación entre el libro y la editorial.

autores = Autor.objects.filter(pk__in=(1,)).prefetch_related("libro__editorial")

# In [4]: autores
# Out[4]: SELECT "libreria_autor"."id",
#        "libreria_autor"."nombre"
#   FROM "libreria_autor"
#  WHERE "libreria_autor"."id" IN (1)
#  LIMIT 21

# Execution time: 0.000000s [Database: default]
# SELECT ("libreria_autorcapitulo"."autor_id") AS "_prefetch_related_val_autor_id",
#        "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_autorcapitulo"
#     ON ("libreria_libro"."id" = "libreria_autorcapitulo"."libro_id")
#  WHERE "libreria_autorcapitulo"."autor_id" IN (1)

# Execution time: 0.002157s [Database: default]
# SELECT "libreria_editorial"."id",
#        "libreria_editorial"."nombre"
#   FROM "libreria_editorial"
#  WHERE "libreria_editorial"."id" IN (1)

# Execution time: 0.000000s [Database: default]
# <QuerySet [<Autor: Jason R. Weiss>]>

# Prefetch al rescate 
 
# Existe una clase llamada Prefetch que podemos usar para controlar un poco mas las operaciones que va a 
# realizar prefetch_related, en esta consulta utilizamos el método select_related que ya habíamos visto en las consultas 
# uno a muchos y esta consulta se la especificamos dentro del Prefectch en su propiedad queryset.

libro_y_editorial = Libro.objects.select_related('editorial')

# Prefetch_related para traer los autores y sus libros, junto con sus editoriales
autores = Autor.objects.filter(pk__in=(1,)).prefetch_related(
    Prefetch('libro', queryset=libro_y_editorial)
)

# Iterar sobre los autores y sus libros
for autor in autores:
    print(f'Autor: {autor}')
    print('Libros escritos:')
    for libro in autor.libro.all():
        print(f'{libro.isbn} - Editorial: {libro.editorial.nombre}')
        
        
#         SELECT "libreria_autor"."id",
#        "libreria_autor"."nombre"
#   FROM "libreria_autor"
#  WHERE "libreria_autor"."id" IN (1)

# Execution time: 0.000000s [Database: default]
# SELECT ("libreria_autorcapitulo"."autor_id") AS "_prefetch_related_val_autor_id",
#        "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id",
#        "libreria_editorial"."id",
#        "libreria_editorial"."nombre"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_autorcapitulo"
#     ON ("libreria_libro"."id" = "libreria_autorcapitulo"."libro_id")
#  INNER JOIN "libreria_editorial"
#     ON ("libreria_libro"."editorial_id" = "libreria_editorial"."id")
#  WHERE "libreria_autorcapitulo"."autor_id" IN (1)

# Execution time: 0.000999s [Database: default]
# Autor: Jason R. Weiss
# Libros escritos:
# 1234567890127 - Editorial: Editorial Ejemplo
# 1234567890127 - Editorial: Editorial Ejemplo
# 1234567890126 - Editorial: Editorial Ejemplo


# Usando los atributos de Prefetch 
# Prefetch nos permite darle un nombre de atributo usando to_attr con lo cual en la consulta anterior podríamos 
# usar este nombre, en este ejemplo pueden ver que no necesitamos llamar autor.libro.all() sino que llamamos 
# autor.libaut, esto no modifica la consulta sql, es la misma del ejemplo anterior. 

# Filtra los libros cuyo título contiene 'u' y selecciona sus editoriales
libro_y_editorial = Libro.objects.filter(titulo__contains='u').select_related('editorial')

# Usa Prefetch con `to_attr='libaut'` para almacenar los libros relacionados en `autor.Jason R. Weiss`
autores = Autor.objects.filter(pk__in=(1,)).prefetch_related(
    Prefetch('libro', queryset=libro_y_editorial, to_attr='Jason R. Weiss')
)

# Itera sobre los autores y sus libros almacenados en `libaut`
# for autor in autores:
#     print(f'Autor: {autor}')
#     print('Libros escritos:')
#     for libro in autor.Jason R. Weiss:
#         print(f'{libro.isbn} - Editorial: {libro.editorial.nombre}')


# Relación inversa 
# Hasta el momento hemos hecho las consultas muchos a muchos teniendo como base el modelo en el cual se especifico 
# la relación, en este caso tomamos como base el modelo Autor y de allí buscamos sus Libros, pero que pasa si queremos 
# realizar la consulta sobre el modelo en el que no esta especificada la relación en este caso es Libro. 
# Para realizar esto hacemos uso del nombre que le pusimos a nuestra relación en related_name='libros_autores', en este 
# ejemplo consultamos algunos Libros y mostramos su Editorial y el Autor o Autores que los escribieron. 

# Filtrar libros por ISBN y seleccionar la editorial
libros = Libro.objects.filter(isbn__in=('1234567890123', '1234567890127')).select_related('editorial').prefetch_related('libros_autores')

# Iterar sobre los libros filtrados
for p in libros:
    print(f'{p.isbn} - {p.titulo} - Editorial: {p.editorial.nombre} - Escrito por:')

    # Iterar sobre los autores de cada libro
    for q in p.libros_autores.all():
        print(f'    {q.nombre}')  # Indentación para una mejor presentación
        
#         SELECT "libreria_libro"."id",
#        "libreria_libro"."isbn",
#        "libreria_libro"."titulo",
#        "libreria_libro"."paginas",
#        "libreria_libro"."fecha_publicacion",
#        "libreria_libro"."imagen",
#        "libreria_libro"."desc_corta",
#        "libreria_libro"."estatus",
#        "libreria_libro"."categoria",
#        "libreria_libro"."editorial_id",
#        "libreria_editorial"."id",
#        "libreria_editorial"."nombre"
#   FROM "libreria_libro"
#  INNER JOIN "libreria_editorial"
#     ON ("libreria_libro"."editorial_id" = "libreria_editorial"."id")
#  WHERE "libreria_libro"."isbn" IN ('1234567890123', '1234567890127')

# Execution time: 0.001009s [Database: default]
# SELECT ("libreria_autorcapitulo"."libro_id") AS "_prefetch_related_val_libro_id",
#        "libreria_autor"."id",
#        "libreria_autor"."nombre"
#   FROM "libreria_autor"
#  INNER JOIN "libreria_autorcapitulo"
#     ON ("libreria_autor"."id" = "libreria_autorcapitulo"."autor_id")
#  WHERE "libreria_autorcapitulo"."libro_id" IN (1, 4)

# Execution time: 0.001337s [Database: default]
# 1234567890123 - Introducción a la Programación - Editorial: Editorial Ejemplo - Escrito por:
# 1234567890127 - Estructuras de Datos - Editorial: Editorial Ejemplo - Escrito por:
#     Jason R. Weiss
#     Jason R. Weiss



# 1. Crea 6 autores y relaciónalos con el libro  “La Fe”. (bulk_create)

libro_lafe = Libro.objects.create(
    isbn='1234567895133',
    titulo='La Fe 2',
    paginas=250,
    fecha_publicacion='2024-10-27',
    imagen='https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0',
    desc_corta='Un libro xd.',
    estatus='B',
    categoria='Referencia',
    editorial=Editorial.objects.get(id=1)
)

Autor.objects.bulk_create([ Autor(nombre="antoni"), Autor(nombre="Autor 7M"), Autor(nombre="Autor 8M"),Autor(nombre="Autor 4M"),Autor(nombre="Autor 5M"), Autor(nombre="Autor 6M")  ])

autor_1 = Autor.objects.get(nombre='antoni')
autor_2 = Autor.objects.get(nombre='Autor 8M')
autor_3 = Autor.objects.get(nombre='Autor 4M')
autor_4 = Autor.objects.get(nombre='Autor 5M')
autor_5 = Autor.objects.get(nombre='Autor 6M')
autor_6 = Autor.objects.get(nombre='Autor 7M')

autor_capitulo_fe = AutorCapitulo.objects.create(
    autor=autor_5,  # Vinculando con el autor existente
    libro=libro_lafe,
    numero_capitulos=6
)

# 2. Encuentra todos los autores con nombres que contengan la letra "o" y que hayan escrito un libro en la categoría "Referencia".



# 3. Busca libros publicados entre los años 2020 y 2024 y con mas de 250 páginas y tengan una categoría diferente de "Referencia".

libros_publicados_2024 = Libro.objects.filter(fecha_publicacion__year=2020).values('isbn', 'fecha_publicacion')

#4.  Dado el libro la “la biblia” mostrar todos sus actores


biblia = Libro.objects.create(
    isbn='1234567896133',
    titulo='La Biblia',
    paginas=250,
    fecha_publicacion='2024-10-27',
    imagen='https://th.bing.com/th/id/R.b165f8fa8de139c95917895c4be688d0?rik=3hndkQ33N9GSQg&pid=ImgRaw&r=0',
    desc_corta='Un libro xd.',
    estatus='B',
    categoria='Referencia',
    editorial=Editorial.objects.get(id=1)
)

autor_b = Autor.objects.get(nombre='Ahmed Sidky')

autor_capitulo_b = AutorCapitulo.objects.create(
    autor=autor_b,  # Vinculando con el autor existente
    libro=biblia,
    numero_capitulos=6
)


#5. Incrementa el número de páginas en 50 para todos los libros que tengan más de 100 páginas y cuyo autor sea “antoni”