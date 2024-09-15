from rest_framework import viewsets
from pagamento.models import pagamento
from .serializer import pagamentoSerializer



class pagamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pagamentos"""
    queryset = pagamento.objects.all()
    serializer_class = pagamentoSerializer

