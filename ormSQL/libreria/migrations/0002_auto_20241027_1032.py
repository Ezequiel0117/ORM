# Generated by Django 5.1.2 on 2024-10-27 15:32

from django.db import migrations

 
def cargar_datos_desde_sql(): 
    from ormSQL.settings import BASE_DIR 
    import os 
    sql_script = open(os.path.join(BASE_DIR,'libreria/sql/migracion.sql'),'r').read() 
    return sql_script

class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(cargar_datos_desde_sql(),)
    ]