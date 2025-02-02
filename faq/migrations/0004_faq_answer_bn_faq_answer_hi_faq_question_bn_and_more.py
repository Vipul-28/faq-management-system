# Generated by Django 5.1.5 on 2025-02-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_alter_faq_answer_alter_faq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
