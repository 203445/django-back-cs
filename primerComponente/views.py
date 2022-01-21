from rest_framework.views import APIView
from rest_framework.response import Response

# Importación de modelos
from primerComponente.models import PrimerModelo

# Importación de serializers
from primerComponente.serializers import PrimerTablaSerializers
# Create your views here.

class PrimerViewList(APIView):
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializers(querySet,many=True ,context={'request':request})
        return Response(serializer.data)