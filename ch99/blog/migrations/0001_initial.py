# Generated by Django 4.0.2 on 2022-02-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('desciption', models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE_DT')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY_DT')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'db_table': 'blog_post',
                'ordering': ('-modify_dt',),
            },
        ),
    ]
