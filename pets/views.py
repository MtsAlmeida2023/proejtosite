from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import views
from .forms import PetsModForm, SectorModForm
from .models import PetsMod, SectorMod
from .support import Dates, BgCardColor


#Instância classes de suporte
dates = Dates() #Classe que possibilita a inclusão dos meses em português para preenchimento dos formulários.
bg_colors = BgCardColor() #Classe que permite a inclusão da cor de fundo do card em cada objeto pet.

def home(request):
    return redirect ('authors:login')

@login_required(login_url='authors:login', redirect_field_name='next')
def panel(request):
    return render(request, 'pets/pages/panel.html')


def petlist(request):
    
    if request.user.is_authenticated: # Se o usuário estiver logado, exibe todos os cães. Caso contrário, apenas os aptos à adoção.

        petlist = PetsMod.objects.all().order_by('name')
    
    else:
        petlist = PetsMod.objects.filter(aptitude='AP').order_by('name')
    
    context = {
        'petlist': petlist,
        'bg_colors': bg_colors.list(petlist)
    }

    return render(request, 'pets/pages/petpage.html', context=context)

@login_required(login_url='authors:login', redirect_field_name='next')
def users(request):
    return render(request, 'pets/pages/users.html')

#Dog Views
@login_required(login_url='authors:login', redirect_field_name='next')
def pet(request):
           
    form = PetsModForm()
    context = {'form': form, 'months': dates.months, 'years': dates.year_list(), 'pet': pet}
    
    return render(request, 'pets/pages/dog_register.html', context=context)

@login_required(login_url='authors:login', redirect_field_name='next')
def pet_create(request):

    form = PetsModForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():    
        gender_vowel = 'a' if form.cleaned_data['sex'] == 'F' else 'o'        
        registered_message = form.cleaned_data['name'] + " cadastrad" + gender_vowel + " com sucesso!"
        
        form.save()
        
        messages.success(request, registered_message)
    
    else:
        messages.error(request, "Algo deu errado! Por favor, repita a operação de cadastro.")
    
    return redirect('pet:pet')

@login_required(login_url='authors:login', redirect_field_name='next')
def pet_view(request, id):

    pet = get_object_or_404(PetsMod, id=id)
    form = PetsModForm(instance=pet)
    bg_colors.random(pet)

    context = {'form': form, 'months': dates.months, 'years': dates.year_list(), 'pet': pet}
    
    return render (request, 'pets/pages/dog_register.html', context=context)

@login_required(login_url='authors:login', redirect_field_name='next')
def pet_update(request, id):
    pet = get_object_or_404(PetsMod, id=id)
    form = PetsModForm(request.POST or None, instance = pet)

    if request.method == 'POST' and form.is_valid():
        
        gender_vowel = 'a' if form.cleaned_data['sex'] == 'F' else 'o'        
        updated_message = form.cleaned_data['name'] + " atualizad" + gender_vowel + " com sucesso!"
        
        form.save()
    
        messages.success(request, updated_message)
    
    else:
        messages.error(request, "Algo deu errado! Por favor, repita a operação de atualização.")
   
    return redirect('pet:pet_view', id=id)

@login_required(login_url='authors:login', redirect_field_name='next')
def pet_delete(request, id):

    pet = get_object_or_404(PetsMod, id=id)
    
    gender_vowel = 'a' if pet.sex == 'F' else 'o'        
    deleted_message = pet.name + " excluid" + gender_vowel + " com sucesso!"
        
    if request.method == 'POST':
        
        messages.success(request, deleted_message) 
        pet.delete()
    
    else:
        messages.error(request, "Algo deu errado! Por favor, repita a operação de exclusão.")
    
    return redirect('pet:panel')

# Sector Views

@login_required(login_url='authors:login', redirect_field_name='next')
def sector_manager(request):
          
    form = SectorModForm()
    
    sectors = SectorMod.objects.annotate(resident_number=Count('petsmod'))
    sector_forms = [ SectorModForm(instance=sector, prefix=str(sector.id)) for sector in sectors ] #Cria uma lista de formulários para a linha retrátil de edição.
    sector_residents = {sector: list(PetsMod.objects.filter(sector=sector.id)) for sector in sectors} #Cria um dicionário com os setores e os pets que estão em cada setor. (P/ FUTURA MELHORIA)
    
    context = {
            'form': form,
            'sectors': sectors,
            'years': dates.year_list(),
            'sector_forms': sector_forms,
            'sector_residents': sector_residents
        }

    return render(request, 'pets/pages/sector_manager.html', context=context)
    
@login_required(login_url='authors:login', redirect_field_name='next')
def sector_create(request):
       
    form = SectorModForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():    
        
        created_message = form.cleaned_data['name'] + " criado com sucesso!"
        messages.success(request, created_message)
        
        form.save()
    
    else:
        messages.error(request, "Algo deu errado! Por favor, repita a operação de criação.")
        
    
    return redirect('pet:sector_manager')

@login_required(login_url='authors:login', redirect_field_name='next')    
def sector_update(request, id):
    
    sector = get_object_or_404(SectorMod, id=id)
    
    form = SectorModForm(request.POST or None, instance = sector)
    
    if request.method == 'POST' and form.is_valid():
        
        updated_message = form.cleaned_data['name'] + " atualizado com sucesso!"
        messages.success(request, updated_message)
        form.save()
    
    else:
         print(form.errors)
         messages.error(request, "Algo deu errado! Por favor, repita a operação de atualização.")
    
    return redirect('pet:sector_manager')

@login_required(login_url='authors:login', redirect_field_name='next')
def sector_delete(request, id):
    
    sector = get_object_or_404(SectorMod, id=id)
    
    if request.method == 'POST':
        sector.delete()
    
    return redirect('pet:sector_manager')

@login_required(login_url='authors:login', redirect_field_name='next')
def search(request):
    
    sectors = SectorMod.objects.all()

    context = {'sectors': sectors, 'aptitudes': PetsMod.APTITUDE }
    
    return render (request, 'pets/pages/search.html', context=context)

@login_required(login_url='authors:login', redirect_field_name='next')
def search_respost(request):
    
    sectors = SectorMod.objects.all()

    context = {'sectors': sectors, 'aptitudes': PetsMod.APTITUDE }
    
    allowed_fields = ['name', 'sex', 'sector', 'aptitude']
    
    if request.method == 'POST':
        
        results = PetsMod.objects.all()

        for key, value in request.POST.items():
            if key in allowed_fields:
                if value:
                    if key == 'name':
                        results = results.filter(name__istartswith=value)
                    else:                
                        results = results.filter(**{key:value})

        context['petlist'] = results
        context['num_results'] = len(results)
        context['bg_colors'] = bg_colors.list(results) 

    return render (request, 'pets/pages/search.html', context=context)