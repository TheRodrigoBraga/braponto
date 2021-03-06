# Generated by Django 3.1.7 on 2021-03-03 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210303_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='core.funcionario', to_field='nome'),
        ),
    ]
