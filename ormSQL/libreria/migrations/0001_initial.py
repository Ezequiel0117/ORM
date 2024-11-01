# Generated by Django 5.1.2 on 2024-10-27 07:41

import django.db.models.deletion
import libreria.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'libreria_editorial',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(default='0000000000000', max_length=13)),
                ('titulo', models.CharField(blank=True, max_length=70, validators=[libreria.models.validar_titulo])),
                ('paginas', models.PositiveIntegerField(default=100)),
                ('fecha_publicacion', models.DateField(null=True)),
                ('imagen', models.URLField(max_length=85, null=True)),
                ('desc_corta', models.CharField(default='Descripción no disponible', max_length=2000)),
                ('estatus', models.CharField(default='A', max_length=1)),
                ('categoria', models.CharField(default='General', max_length=50)),
                ('editorial', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='libreria.editorial')),
            ],
        ),
        migrations.CreateModel(
            name='LibroCronica',
            fields=[
                ('descripcion_larga', models.TextField(null=True)),
                ('libro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='libreria.libro')),
            ],
        ),
        migrations.CreateModel(
            name='AutorCapitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_capitulos', models.IntegerField(default=1)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libreria.autor')),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libreria.libro')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libro',
            field=models.ManyToManyField(related_name='libros_autores', through='libreria.AutorCapitulo', to='libreria.libro'),
        ),
        migrations.AddConstraint(
            model_name='libro',
            constraint=models.CheckConstraint(condition=models.Q(('titulo', 'cobol'), _negated=True), name='titulo_no_permitido_chk'),
        ),
    ]
