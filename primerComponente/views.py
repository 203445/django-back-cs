from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

# Importación de modelos
from primerComponente.models import PrimerModelo

# Importación de serializers
from primerComponente.serializers import PrimerTablaSerializers
# Create your views here.

#variables globales
responseOk =  '{ "messages":"success"}'
responseOk = json.loads(responseOk)

responseBad =  '{ "messages":"error"}'
responseBad = json.loads(responseBad)

result = {}

class PrimerViewList(APIView):
    
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializers(querySet,many=True ,context={'request':request})
        return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))

    def post(self, request, format=None):
        serializer = PrimerTablaSerializers(data = request.data, context={'request':request})   
        if serializer.is_valid():
            serializer.save()
            
            return Response(responseView.response_custom(serializer.data,status.HTTP_201_CREATED,'responseok'))
        else:
            return Response(responseView.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'responsebad'))
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
            return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))
        else:
            return Response(responseView.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'responsebad'))  
    
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)

        if idResponse != 404:
            serializer = PrimerTablaSerializers(idResponse, data = request.data ,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))
            else:
                return Response(responseView.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'responsebad')) 
        else:
            return Response(responseView.response_custom('ID no encontrado',status.HTTP_400_BAD_REQUEST,'responsebad')) 

    def delete (self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse !=404:
            idResponse.delete()
            #serializer = PrimerTablaSerializers(idResponse, data = request.data ,context={'request': request})
            # return Response(responseView.response_custom(serializer.data,status.HTTP_204_NO_CONTENT,'responseok'))
            # if serializer.is_valid():
            #     serializer.save()
                # serializer.delete()
            return Response(responseView.response_custom('Dato eliminado',status.HTTP_200_OK,'responseok'))
            # else:
            #     return Response(responseView.response_custom(serializer.errors, status.HTTP_400_BAD_REQUEST,'responsebad'))
        else:
            return Response(responseView.response_custom('ID no encontrado', status.HTTP_400_BAD_REQUEST,'responsebad'))

class responseView(APIView):
    def  response_custom(dater,st,responseTwo):
        if responseTwo == "responseok":
            result = responseOk
        else:
            result = responseBad    
        result.update({'pay_load': dater,'status': st})
        return result