from django.urls import path, include,re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.conf import settings
from django.views.static import serve   


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']
  
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^api/', include('Login.urls')),
    re_path(r'^api/v1/primer_componente/', include('primerComponente.urls')),
    re_path(r'^api/', include('registro.urls')), 
    re_path(r'^api/v1/loadImage/', include('loadImage.urls')),
    re_path(r'^api/v1/', include('profileUser.urls')), 


]
urlpatterns += [ re_path(r'^assets/(?P<path>.*)$', serve,{ 'document_root' :settings.MEDIA_ROOT,
}),]

