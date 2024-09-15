from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [ ]

    operations = [
        migrations.CreateModel(
            name='pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField()),
                ('permite_recorrencia', models.BooleanField((""))),
                ('quantidade_recorrencia', models.IntegerField((""))),
                ('intervalo_recorrencia',  models.IntegerField((""))),
                ('status_recorrencia', models.TextField((""))),
                ('agencia', models.IntegerField((""))),
            ],
        ),    
    ]
