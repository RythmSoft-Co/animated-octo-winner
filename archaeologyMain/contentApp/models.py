from django.db import models

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

import datetime, string


class Fixture(models.Model):
    name = models.CharField(("Demirbaş Adı"), max_length=150)
    marka = models.CharField(("Marka"), max_length=150)
    model = models.CharField(("Model"), max_length=150)
    piece = models.IntegerField(("Adet"))
    unitprice = models.DecimalField(("Birim Fiyatı"), max_digits=15, decimal_places=2)
    taxrate = models.DecimalField(("Vergi Oranı"), max_digits=5, decimal_places=2)
    totalprice = models.DecimalField(("Toplam Fiyat"), max_digits=15, decimal_places=2)
    typeofaddition = models.CharField(("Alış Şekli"), max_length=150)
    dateofaddition = models.DateField(("Alım Tarihi"), auto_now_add=True)
    where = models.CharField(("Bulunduğu Yer"), max_length=150)
    custodian = models.CharField(("Zimmetli Kişi"), max_length=150)
    barcode = models.CharField(("Barkod Numarası"), max_length=150)

    def __str__(self) -> str:
        return self.name
    
class CompanyInfo(models.Model):
    fixture = models.ForeignKey(Fixture, verbose_name=("Demirbaş"), on_delete=models.CASCADE)
    companyName = models.CharField(("Firma Adı"), max_length=150)
    companyOfficial = models.CharField(("Firma Yetkilisi"), max_length=150)
    companyPhone = models.CharField(("Firma Adı"), max_length=150)
    companyEmail = models.EmailField(("Firma E-Mail"), max_length=254)
    companyAddress = models.TextField(("Firma Adresi"))

    def __str__(self) -> str:
        return self.companyName
    

class FixtureInfo(models.Model):
    fixture = models.ForeignKey(Fixture, verbose_name=("Demirbaş"), on_delete=models.CASCADE)
    fixtureFile = models.FileField(("Demirbaş Alım Belgesi"), upload_to="fixture", max_length=100)
    fixtureDescription = RichTextField(("Demirbaş Açıklama"),max_length=900)

    def __str__(self) -> str:
        return self.fixture
    



"""
Aşağıdaki modeller buluntu kayıt form genel bilgiler'i kapsar
"""

# util functions
def avaiable_years():
    return [(y,y) for y in range(1991, datetime.date.today().year + 1)]

def current_year():
    return datetime.date.today().year


# PLANKARE X
def generate_letters():
    
    combinations = []
    alphabet = string.ascii_uppercase

    for first_char in alphabet:
        combinations.append(first_char)

    else:
      for first_char in alphabet:
          for second_char in alphabet:
              current_combination = first_char + second_char
              combinations.append(current_combination)

               # AZ'ye ulaştıysak işlemi durdur
              if current_combination == 'AZ':
                  return [(char, char) for char in combinations]
    
      return combinations

# PLANKARE Y
def generate_numbers():
    return [(number,number) for number in range(1, 101)]

# end of util functions


"""
BuluntuTypes => Keramik, Kemik, taş, kücüktas vs.
"""

class BuluntuTypes(models.Model):

    buluntu = models.CharField(("Buluntu Türü"), max_length=30)

    def __str__(self) -> str:
        return self.buluntu


"""
BuluntuAlani => Pulluk, Çukur, Yapı İçi vs. 
"""

class BuluntuAlani(models.Model):

    alan = models.CharField(("Alan"), max_length=50)

    def __str__(self) -> str:
        return self.alan
    
"""
Buluntu Dönemi Burada Ayarlanır
"""

class BuluntuPeriod(models.Model):

    period = models.CharField(("Dönem"), max_length=50)

    def __str__(self) -> str:
        return self.period

class SetGeneralBuluntu(models.Model):
       
    # methods
    year_choices = avaiable_years()
    letter_choices = generate_letters()
    number_choices = generate_numbers()
       
    year = models.IntegerField(('Yıl Bilgisi'), choices=year_choices, default=current_year)
    date = models.DateField(("Buluntu Tarihi"), auto_now=False)
    plankareX = models.CharField(("Plankare X"), max_length=4, choices=letter_choices, default="A")
    plankareY = models.IntegerField(('Plankare Y'), choices=number_choices, default=1)

    gridX = models.CharField(("Grid X"), max_length=50)
    gridY = models.CharField(("Grid Y"), max_length=50)
    no = models.IntegerField(("Buluntu No"))
    secondaryNo = models.IntegerField(("Küçük Buluntu No"))



    type = models.ForeignKey("contentApp.BuluntuTypes", verbose_name=("Tür"), on_delete=models.CASCADE)


    nivo = models.CharField(("Açılış Nivosu"), max_length=50)
    nivo_h = models.CharField(("Açılış Nivosu H"), max_length=50)
    shut_nivo = models.CharField(("Kapanış Nivosu"), max_length=50)
    shut_nivo_h = models.CharField(("Kapanış Nivosu H"), max_length=50)

    kor_x = models.CharField(("Kordinat X"), max_length=50)
    kor_y = models.CharField(("Kordinat Y"), max_length=50)
    kor_h = models.CharField(("Kordinat H"), max_length=50)

    area = models.ManyToManyField("contentApp.BuluntuAlani", verbose_name=("Buluntu / Kova Alanı"))
    colour = ColorField(default='#FF0000', verbose_name="Renk")
    
    layer_count = models.CharField(("Tabaka Sayı"), max_length=50)
    layer_letter = models.CharField(("Tabaka Harf"), max_length=50)
    phase = models.CharField(("Evre"), max_length=50)
    period = models.ForeignKey("contentApp.BuluntuPeriod", verbose_name=("Dönem"), on_delete=models.CASCADE)


    # def __str__(self) -> str:
    #     return self.no