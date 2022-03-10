from django.urls import re_path

# Importando vistas
from profileUser .views import PrimerViewList,PrimerViewDetail

urlpatterns = [
    re_path(r'^profile/$', PrimerViewList.as_view()), 
    re_path(r'^profile/(?P<pk>\d+)$', PrimerViewDetail.as_view()),   
]   