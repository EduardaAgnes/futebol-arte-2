from django.contrib import admin
from .models import Pais,Estado,Cidade 

class estadoinline(admin.StackedInline):
    model = Estado
    extra = 0 

class cidadeinline(admin.StackedInline):
    model = Cidade
    extra = 0     

@admin.register(Estado)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['estado']
    inlines = [cidadeinline] 
        
@admin.register(Pais)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['pais']
    inlines = [estadoinline]
        
@admin.register(Cidade)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['cidade']
