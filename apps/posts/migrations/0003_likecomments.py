# Generated by Django 4.1.7 on 2023-07-26 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_post_options_like_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_user', to=settings.AUTH_USER_MODEL)),
                ('to_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_comment', to='posts.comment')),
            ],
            options={
                'verbose_name': 'Лайк для коммента',
                'verbose_name_plural': 'Лайки для комментарий',
            },
        ),
    ]
