# Generated by Django 3.2.9 on 2021-11-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.bank', verbose_name='Bank'),
        ),
    ]
