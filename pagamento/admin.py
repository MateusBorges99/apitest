from django.contrib import admin
from pagamento.models import pagamento

class pagamentos(admin.ModelAdmin):
    list_display = ("id", "data_pagamento", "permite_recorrencia","quantidade_recorrencia","intervalo_recorrencia",
                    "status_recorrencia", "agencia", "conta", "valor")
    list_display_links = ('id')
    search_fields = ('id')
    list_per_page = 20








