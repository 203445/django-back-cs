from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

    def post(self, request, format=None):
        serializer = PrimerTablaSerializers(data = request.data, context={'request':request})  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class PrimerViewDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk = pk)
        except PrimerModelo.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = PrimerTablaSerializers(idResponse, context={'request': request})
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)

        if idResponse != 404:
            serializer = PrimerTablaSerializers(idResponse, data = request.data ,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
        else:
            return Response('ID no encontrado', status = status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk = pk)
       
        if idResponse != 404:
            idResponse.delete()
            return Response({'message': 'usuario eliminado correctamente'})
        else:
            return Response('ID no encontrado', status =  status.HTTP_404_NOT_FOUND) 
      