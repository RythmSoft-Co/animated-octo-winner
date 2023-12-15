from django import forms
from django.forms import DateInput
from .models import *

class CustomDateInput(DateInput):
    input_type = 'date'

class FixtureForm(forms.ModelForm):

    class Meta:
        model = Fixture
        fields = ["name","marka","model","piece","unitprice","taxrate","totalprice","typeofaddition","dateofaddition","where","custodian","barcode"]
        widgets = {
            'dateofaddition': CustomDateInput(),
        }
    def __init__(self, *args, **kwargs):
        super(FixtureForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Tüm alanlara form-control sınıfını ekler
            if field_name == 'dateofaddition':
                field.widget.attrs['input_type'] = 'date'
            field.widget.attrs['class'] = 'form-control mb-3 rounded'
            
            # Alan adına göre etiket ekler
            field.widget.attrs['placeholder'] = field.label