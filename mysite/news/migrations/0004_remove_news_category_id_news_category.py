# Generated by Django 4.2 on 2023-05-03 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_news_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category_id',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
        ),
    ]
