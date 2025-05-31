from django import forms
from .models import PetsMod, SectorMod

class PetsModForm(forms.ModelForm):
    class Meta:
        model = PetsMod
        fields = ['name', 'sex', 'birth', 'breed', 'size', 'sector', #dados basicos 
                  'vaccine', 'vermifuge', 'aptitude', #dados de tratamento
                  'front_photo','side_photo', 'size_photo'] # fotos
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-center form-field-lg', 'placeholder': 'Nome do cão'}),
                   'sex': forms.RadioSelect(attrs={'class': 'form-check-input ms-3 me-2'}),
                   #linha em branco para o nascimento
                   'breed': forms.TextInput(attrs={'class': 'form-control text-center form-field-lg', 'value': 'Sem raça definida'}),
                   'size': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'sector': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'aptitude': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'front_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'frontPreview')"}),
                   'side_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'sidePreview')"}),
                    'size_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'sizePreview')"})
                    }
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['front_photo'].widget.initial_text = 'Foto atual'
        self.fields['front_photo'].widget.input_text = 'Escolher outra'

        self.fields['size_photo'].widget.initial_text = 'Foto atual'
        self.fields['size_photo'].widget.input_text = 'Escolher outra'

        self.fields['side_photo'].widget.initial_text = 'Foto atual'
        self.fields['side_photo'].widget.input_text = "Escolher outra"

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.capitalize()

    def clean_breed(self):
        breed = self.cleaned_data.get('breed','')
        return breed.capitalize()

class SectorModForm(forms.ModelForm):
    class Meta:
        model = SectorMod
        fields = ['name', 'type']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-center field-add-sector', 'placeholder': 'Nome do setor'}),
                     'type': forms.Select(attrs={'class': 'form-select text-center field-add-type'})        
                   }
        
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.capitalize()
