from rest_framework import serializers

#importación de modelos
from loadImage.models import imageLoad

class segundaTablaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = imageLoad
        fields = ('__all__')
