# Generated by Django 3.2.10 on 2021-12-12 22:22

from django.db import migrations, models
import django.db.models.deletion
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sub_title', models.CharField(blank=True, max_length=600)),
                ('body', wagtailmarkdown.fields.MarkdownField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blog_image', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sub_title', models.CharField(blank=True, max_length=600)),
                ('body', wagtailmarkdown.fields.MarkdownField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blog_index_image', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]