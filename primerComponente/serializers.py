from rest_framework import serializers

#importación de modelos
from primerComponente.models import PrimerModelo

class PrimerTablaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrimerModelo
        fields = ('__all__')