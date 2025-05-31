from django.db import models
from django.forms import MultiWidget, TextInput
from django.contrib.auth.models import User
from datetime import date


class SectorMod(models.Model):
        TYPE = [("I", "Individual"), ("C", "Coletivo")] #Criando as opções de escolha para o tipo de setor

        name= models.CharField(max_length=65)
        type = models.CharField(max_length=1, choices=TYPE, default="C")
        def __str__(self):
            return self.name
        
class PetsMod(models.Model):
        
        #Criando as opções de escolha para o sexo, porte e aptidão do animal.
        
        APTITUDE = [("AP", "Apto"), ("IN", "Inapto"), ("PR", "Em preparo"), ("AD", "Adotado")]
        SEXES = [("M", "Macho"), ("F", "Fêmea")]
        SIZES = [("P", "Pequeno"), ("PM", "Peq/Médio"), ("M", "Médio"), ("MG", "Med/Grande"), ("G", "Grande")]
        MONTHS_PT = {1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN", 7: "JUL", 8: "AGO",
        9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"}

        #Como passar o setor para cá como variável para preencher o campo de setor?
        
        #Campos em si na mesma ordem em que aparecem no formulário.
        
        #Dados básicos do cão
        name = models.CharField(max_length=100)
        sex = models.CharField(max_length=1, choices=SEXES, default="M")
        birth = models.DateField(auto_now=False, auto_now_add=False)
        
        breed = models.CharField(max_length=100, blank=True, null=True) 
        size = models.CharField(max_length=2, choices=SIZES, default="P")
        sector = models.ForeignKey(SectorMod, on_delete=models.SET_NULL, null=True)
        
        #Dados de tratamento

        vaccine = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
        vermifuge = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
        aptitude = models.CharField(max_length=2, choices=APTITUDE, default="AP")

        #Fotos      
        front_photo = models.ImageField(upload_to='pets/photos/front/%y/%m/%d/')
        side_photo = models.ImageField(upload_to='pets/photos/side/%y/%m/%d/', blank=True, null=True)
        size_photo = models.ImageField(upload_to='pets/photos/size/%y/%m/%d/', blank=True, null=True)
        
        #Metadados
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return self.name
        
        def get_month_abbr(self, field):
            date_value = getattr(self, field, None)
            if date_value:
                    return self.MONTHS_PT[date_value.month]
            return ""
        
        #PERMITE CHAMAR OS MESES EM PORTUGUES COMO UMA PROPRIEDADE DO MODELO
        @property
        def birth_month_abbr(self):
            return self.get_month_abbr("birth")

        @property
        def vaccine_month_abbr(self):
            return self.get_month_abbr("vaccine")

        @property
        def vermifuge_month_abbr(self):
            return self.get_month_abbr("vermifuge")