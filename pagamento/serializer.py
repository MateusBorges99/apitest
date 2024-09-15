from rest_framework.serializers import ModelSerializer
from pagamento.models import pagamento

def clean_valor(self):  
        valor = self.cleaned_data['valor']  
        return int(valor)
    
class pagamentoSerializer(ModelSerializer):   
    class Meta:
        model = pagamento
        fields = ["id", "data_pagamento", "permite_recorrencia","quantidade_recorrencia","intervalo_recorrencia",
                    "status_recorrencia", "agencia", "conta", "valor",
]
    
    
       