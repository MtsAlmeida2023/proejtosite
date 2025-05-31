from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pet"

urlpatterns = [
    path('', views.home, name='home'),
    path('panel', views.panel, name='panel'), #teste da nova página
    path('users', views.users, name='users'),
    
    # Pet URLs
    
    path('pet', views.pet, name='pet'),
    path('pet/create', views.pet_create, name='pet_create'),
    path('pet/view/<int:id>', views.pet_view, name='pet_view'),
    path('pet/update/<int:id>', views.pet_update, name='pet_update'),
    path('pet/delete/<int:id>', views.pet_delete, name='pet_delete'),
    
    path('petlist', views.petlist, name='petlist'),
    
    ## Sector URLs
    path('sector', views.sector_manager, name='sector_manager'),
    path('sector/create', views.sector_create, name='sector_create'),
    path('sector/update/<int:id>', views.sector_update, name='sector_update'),
    path('sector/delete/<int:id>', views.sector_delete, name='sector_delete'),

    #Search URLs
    path('search', views.search, name='search'),
    path('search_respost', views.search_respost, name='search_respost')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)