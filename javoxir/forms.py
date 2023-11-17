from django import forms
from javoxir.models import UzAuto


class AddAuto(forms.ModelForm):
    class Meta:
        model = UzAuto
        fields = ['nomi', 'rangi', 'narxi']



class EditAuto(forms.ModelForm):
    class Meta:
        model = UzAuto
        fields = ['nomi', 'rangi', 'narxi']