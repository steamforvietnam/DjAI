# Generated by Django 3.2 on 2021-04-14 09:13


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = ('DjAIModel', '0001_AIModel'),

    operations = \
        migrations.CreateModel(
            name='SKLModel',

            fields=[
                ('aimodel_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    related_name='skl_models',
                    serialize=False, to='DjAIModel.aimodel')),

                ('artifact',
                 models.BinaryField(
                    default=None,
                    help_text='Model Artifact (raw binary data)',
                    verbose_name='Model Artifact (raw binary data)'))
            ],

            options={
                'verbose_name': 'SciKit-Learn Model',
                'verbose_name_plural': 'SciKit-Learn Models',
                'db_table': 'DjAIModel_SKLModel',
                'abstract': False,
                'default_related_name': 'skl_models',
                'base_manager_name': 'objects'
            },

            bases=('DjAIModel.aimodel',)
        ),