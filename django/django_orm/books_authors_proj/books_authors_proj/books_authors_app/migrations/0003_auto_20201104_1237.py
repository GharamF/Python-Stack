# Generated by Django 2.2.4 on 2020-11-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20201104_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='notes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Books'),
        ),
    ]
