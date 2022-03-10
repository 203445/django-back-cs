from rest_framework import serializers

#importación de modelos
from profileUser.models import Profileimage

class terceraTablaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Profileimage
        fields = ('__all__')


