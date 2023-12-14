# Generated by Django 5.0 on 2023-12-14 13:40

import ckeditor.fields
import colorfield.fields
import contentApp.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuluntuAlani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alan', models.CharField(max_length=50, verbose_name='Alan')),
            ],
        ),
        migrations.CreateModel(
            name='BuluntuPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=50, verbose_name='Dönem')),
            ],
        ),
        migrations.CreateModel(
            name='BuluntuTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buluntu', models.CharField(max_length=30, verbose_name='Buluntu Türü')),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Demirbaş Adı')),
                ('marka', models.CharField(max_length=150, verbose_name='Marka')),
                ('model', models.CharField(max_length=150, verbose_name='Model')),
                ('piece', models.IntegerField(verbose_name='Adet')),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Birim Fiyatı')),
                ('taxrate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Vergi Oranı')),
                ('totalprice', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Toplam Fiyat')),
                ('typeofaddition', models.CharField(max_length=150, verbose_name='Alış Şekli')),
                ('dateofaddition', models.DateField(auto_now_add=True, verbose_name='Alım Tarihi')),
                ('where', models.CharField(max_length=150, verbose_name='Bulunduğu Yer')),
                ('custodian', models.CharField(max_length=150, verbose_name='Zimmetli Kişi')),
                ('barcode', models.CharField(max_length=150, verbose_name='Barkod Numarası')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=150, verbose_name='Firma Adı')),
                ('companyOfficial', models.CharField(max_length=150, verbose_name='Firma Yetkilisi')),
                ('companyPhone', models.CharField(max_length=150, verbose_name='Firma Telefon')),
                ('companyEmail', models.EmailField(max_length=254, verbose_name='Firma E-Mail')),
                ('companyAddress', models.TextField(verbose_name='Firma Adresi')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentApp.fixture', verbose_name='Demirbaş')),
            ],
        ),
        migrations.CreateModel(
            name='FixtureInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixtureFile', models.FileField(upload_to='fixture', verbose_name='Demirbaş Alım Belgesi')),
                ('fixtureDescription', ckeditor.fields.RichTextField(max_length=900, verbose_name='Demirbaş Açıklama')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentApp.fixture', verbose_name='Demirbaş')),
            ],
        ),
        migrations.CreateModel(
            name='SetGeneralBuluntu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=contentApp.models.current_year, verbose_name='Yıl Bilgisi')),
                ('date', models.DateField(verbose_name='Buluntu Tarihi')),
                ('plankareX', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z'), ('AA', 'AA'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('AF', 'AF'), ('AG', 'AG'), ('AH', 'AH'), ('AI', 'AI'), ('AJ', 'AJ'), ('AK', 'AK'), ('AL', 'AL'), ('AM', 'AM'), ('AN', 'AN'), ('AO', 'AO'), ('AP', 'AP'), ('AQ', 'AQ'), ('AR', 'AR'), ('AS', 'AS'), ('AT', 'AT'), ('AU', 'AU'), ('AV', 'AV'), ('AW', 'AW'), ('AX', 'AX'), ('AY', 'AY'), ('AZ', 'AZ')], default='A', max_length=4, verbose_name='Plankare X')),
                ('plankareY', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100)], default=1, verbose_name='Plankare Y')),
                ('gridX', models.CharField(max_length=50, verbose_name='Grid X')),
                ('gridY', models.CharField(max_length=50, verbose_name='Grid Y')),
                ('no', models.IntegerField(verbose_name='Buluntu No')),
                ('secondaryNo', models.IntegerField(verbose_name='Küçük Buluntu No')),
                ('nivo', models.CharField(max_length=50, verbose_name='Açılış Nivosu')),
                ('nivo_h', models.CharField(max_length=50, verbose_name='Açılış Nivosu H')),
                ('shut_nivo', models.CharField(max_length=50, verbose_name='Kapanış Nivosu')),
                ('shut_nivo_h', models.CharField(max_length=50, verbose_name='Kapanış Nivosu H')),
                ('kor_x', models.CharField(max_length=50, verbose_name='Kordinat X')),
                ('kor_y', models.CharField(max_length=50, verbose_name='Kordinat Y')),
                ('kor_h', models.CharField(max_length=50, verbose_name='Kordinat H')),
                ('colour', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None, verbose_name='Renk')),
                ('layer_count', models.CharField(max_length=50, verbose_name='Tabaka Sayı')),
                ('layer_letter', models.CharField(max_length=50, verbose_name='Tabaka Harf')),
                ('phase', models.CharField(max_length=50, verbose_name='Evre')),
                ('area', models.ManyToManyField(to='contentApp.buluntualani', verbose_name='Buluntu / Kova Alanı')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentApp.buluntuperiod', verbose_name='Dönem')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contentApp.buluntutypes', verbose_name='Tür')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]