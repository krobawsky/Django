# Generated by Django 2.1.2 on 2018-10-30 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200)),
                ('fecha_pub', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.Pregunta'),
        ),
    ]
