# Generated by Django 3.1.1 on 2020-09-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pictureProduct', models.ImageField(default='default/default1.png', upload_to='products/')),
            ],
        ),
    ]
