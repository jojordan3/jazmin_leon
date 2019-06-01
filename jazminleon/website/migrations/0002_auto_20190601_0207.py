# Generated by Django 2.0.13 on 2019-06-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='reply_address',
            field=models.CharField(blank=True, help_text='Optional - to reply to the submitter, specify the email field here. For example, if a form field above is labeled "Your Email", enter: {{ your_email }}', max_length=255, verbose_name='Reply-to address'),
        ),
    ]