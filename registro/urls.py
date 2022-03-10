from django.urls import path, re_path
from django.conf.urls import include


from registro.views import RegisterView, RegisterViewNew

urlpatterns = [
    re_path(r'^v1/register/', RegisterView.as_view()),
    re_path(r'^v2/register/', RegisterViewNew.as_view()),
     re_path(r'^v2/register/(?P<pk>\d+)$', RegisterViewNew.as_view()),
    
]