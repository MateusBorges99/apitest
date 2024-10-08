# Generated by Django 5.1.1 on 2024-09-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0003_alter_pagamento_status_recorrencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='conta',
            field=models.IntegerField(default=1, verbose_name=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagamento',
            name='valor',
            field=models.FloatField(default=1, verbose_name=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='data_pagamento',
            field=models.DateField(auto_now_add=True),
        ),
    ]
