# Generated by Django 4.1.7 on 2023-06-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_emailcheckcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcheckcode',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]