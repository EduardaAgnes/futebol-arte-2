from django.contrib import admin
from core.models import Clube, Jogador, Competicao, Titulo
from django.utils.html import format_html


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    def imagem_tag(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}"; width="60" height="60" />')
    
    list_display = ['nome', 'imagem_tag','ano_de_fundacao', 'divisao', 'cidade', 'estado', 'pais', 'modalidade', 'cores', 'tem_mundial']
    list_filter=['nome','modalidade','estado','tem_mundial','ano_de_fundacao']
    search_fields=['nome','modalidade','estado','cores','ano_de_fundacao']

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    def imagem_tag(self, obj):
        if obj.foto:
            return format_html(f'<img src="{obj.foto.url}"; width="60" height="60" />')

    list_display=['nome','clube','posicao','numero_da_camisa','sexo','imagem_tag']
    list_filter=['nome','clube','posicao','numero_da_camisa']
    search_fields=['nome','clube','posicao','numero_da_camisa','sexo','imagem_tag']

@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):    
    list_display=['nome','tipo','categoria']
    list_filter=['nome','tipo','categoria']
    search_fields=['nome','tipo','categoria']

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):    
    list_display=['ano_da_conquista','data_exata','colocacao']
    list_filter=['ano_da_conquista','data_exata','colocacao']
    search_fields=['ano_da_conquista','data_exata','colocacao']    