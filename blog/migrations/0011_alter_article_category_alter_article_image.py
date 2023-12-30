# Generated by Django 5.0 on 2023-12-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('DEFAULT', 'Default'), ('FEEDS', 'Feeds')], default='DEFAULT', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='Cat03.jpg', null=True, upload_to='media/'),
        ),
    ]