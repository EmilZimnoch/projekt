from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError

from strona.models import TypeOfSpot, Spot, Smart, Service, Room, ROOMS, METERS


#class ServiceForm(forms.Form):
#    square_meters = forms.ModelChoiceField(queryset=METERS.count())
#    rooms = forms.ModelChoiceField(queryset=ROOMS.count())
#    price = forms.IntegerField()



class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        labels = {'name':'Nazwa zleceniodawcy',
                  'square_meters':'Metraż'}


class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        labels = {'name':'Typ pomieszczenia',
                  'service':'Usługa'}


class SmartModelForm(forms.ModelForm):
    class Meta:
        model = Smart
        fields = '__all__'
        labels = {'name':'Nazwa zestawu',
                  'description':'Opis',
                  'smart':'Docelowa usługa'}


class TypeOfSpotModelForm(forms.ModelForm):
    class Meta:
        model = TypeOfSpot
        fields = '__all__'
        labels = {'wall_type':'Typ ściany',
                  'description':'Opis'}


class SpotModelForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields = '__all__'
        labels = {'type':'Typ punktu',
                  'room':'Miejsce montażu',
                  'furrowing':'Rodzaj ściany'}