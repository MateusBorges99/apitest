from django.contrib import admin
from django.urls import path,include
from pagamento.views import pagamentoViewSet, pagamentoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'agendamentos', pagamentoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls) )
    
]
