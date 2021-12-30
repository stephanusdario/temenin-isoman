

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penyakit', models.CharField(max_length=100)),
                ('penjelasan', models.CharField(max_length=1000)),
                ('daftar_obat', models.CharField(max_length=1000)),
            ],
        ),
    ]
