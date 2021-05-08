# Generated by Django 3.1.7 on 2021-05-08 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Chat', '0003_auto_20210508_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'چت', 'verbose_name_plural': 'چت ها'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AddField(
            model_name='message',
            name='related_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Chat.chat', verbose_name='گروه مقصد'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='ممبرها'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='room_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='نام اتاق'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='محتوا'),
        ),
    ]
