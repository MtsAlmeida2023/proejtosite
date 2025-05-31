from django.contrib import admin
from .models import PetsMod, SectorMod
# Register your models here.
class Setoradmin(admin.ModelAdmin):
    ...

admin.site.register(SectorMod, Setoradmin)
class adminpets(admin.ModelAdmin):
    ...
admin.site.register(PetsMod)

