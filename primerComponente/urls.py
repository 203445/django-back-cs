from django.urls import re_path

# Importando vistas
from primerComponente.views import PrimerViewList
from primerComponente.views import PrimerViewDetail
from primerComponente.views import responseView


urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()), 
    re_path(r'^lista/(?P<pk>\d+)$', PrimerViewDetail.as_view()),
    re_path(r'^lista/$', responseView.as_view()),   
]
