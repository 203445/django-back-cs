from django.urls import re_path

# Importando vistas
from loadImage.views import PrimerViewList
from loadImage.views import PrimerViewDetail


urlpatterns = [
    re_path(r'^listaImage/$', PrimerViewList.as_view()), 
    re_path(r'^listaImage/(?P<pk>\d+)$', PrimerViewDetail.as_view()),
    #re_path(r'^lista/$', responseView.as_view()),   
]
