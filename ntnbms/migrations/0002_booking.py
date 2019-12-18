# Generated by Django 2.2.8 on 2019-12-18 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ntnbms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('BID', models.IntegerField(primary_key=True, serialize=False)),
                ('Recipient_Name', models.CharField(max_length=25)),
                ('Air_Time', models.DateTimeField(blank=True, null=True)),
                ('Number_Of_Showing', models.IntegerField()),
                ('Text_Content', models.TextField(blank=True)),
                ('Image_File', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('Air_Date', models.DateField(blank=True, null=True)),
                ('Date_Created', models.DateField(blank=True, null=True)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ntnbms.customer')),
            ],
        ),
    ]