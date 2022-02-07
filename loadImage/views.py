from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from primerComponente.views import responseView

#importanciones necesarias
from posixpath import split
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.conf import settings
import os 


# Importación de modelos
from loadImage.models import imageLoad

# Importación de serializers
from loadImage.serializers import segundaTablaSerializers
# Create your views here.




class PrimerViewList(APIView):

    def get(self, request, format=None):
        querySet = imageLoad.objects.all()
        serializer = segundaTablaSerializers(querySet,many=True ,context={'request':request})
        return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))
    
    def post(self, request, format=None):
        serializer = segundaTablaSerializers(data = request.data, context={'request':request})  
       
        urlimg = request.data
            #urlimg = urlimg.split(".")
        filename = str(urlimg.__getitem__('url_img')).split(".")
        urlimg.__setitem__('name_img', filename[0])
        urlimg.__setitem__('format_img', filename[1])
        serializertwo = segundaTablaSerializers(data = urlimg, context={'request':request})

        if serializertwo.is_valid():    
            serializertwo.save()
  
            return Response(responseView.response_custom(serializertwo.data,status.HTTP_201_CREATED,'responseok'))
        else:
            return Response(responseView.response_custom(serializertwo.errors,status.HTTP_400_BAD_REQUEST,'responsebad'))
           # return Response(serializer.data, status = status.HTTP_200_OK)


class PrimerViewDetail(APIView):
    def get_object(self, pk):
        try:
            return imageLoad.objects.get(pk = pk)
        except imageLoad.DoesNotExist:
            return 404

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = segundaTablaSerializers(idResponse, context={'request': request})
            return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))
        else:
            return Response(responseView.response_custom('ID no encontrado',status.HTTP_400_BAD_REQUEST,'responsebad'))  
    
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)

        if idResponse != 404:
            serializer = segundaTablaSerializers(idResponse, data = request.data ,context={'request': request})
           
            #Eliminar imagen antes de modifar
            fotos = get_object_or_404(imageLoad, pk = pk)
            partes = (fotos.url_img.url).split("/")
            ratok = "\\" +str(partes[2])+ "\\"+ str(partes[3])
            os.remove(os.path.join(settings.MEDIA_ROOT  + ratok))
            fotos.delete()

            #Modificar los datos
            urlimg = request.data
            #urlimg = urlimg.split(".")
            filename = str(urlimg.__getitem__('url_img')).split(".")
            urlimg.__setitem__('edited', timezone.now())
            urlimg.__setitem__('name_img', filename[0])
            urlimg.__setitem__('format_img', filename[1])

            serializertwo = segundaTablaSerializers(idResponse, data = urlimg, context={'request':request})
            if serializertwo.is_valid():
                serializertwo.save()
                return Response(responseView.response_custom(serializertwo.data,status.HTTP_200_OK,'responseok'))
            else:
                return Response(responseView.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'responsebad')) 
        else:
            return Response(responseView.response_custom('ID no encontrado',status.HTTP_400_BAD_REQUEST,'responsebad')) 

    def delete (self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse !=404:
           
            fotos = get_object_or_404(imageLoad, pk = pk)
            partes = (fotos.url_img.url).split("/")
            ratok = "\\" +str(partes[2])+ "\\"+ str(partes[3])
            os.remove(os.path.join(settings.MEDIA_ROOT  + ratok))
            #serializer = PrimerTablaSerializers(idResponse, data = request.data ,context={'request': request})
            # return Response(responseView.response_custom(serializer.data,status.HTTP_204_NO_CONTENT,'responseok'))
            # if serializer.is_valid():
            #     serializer.save()
                # serializer.delete()
            fotos.delete()
            idResponse.delete()
            return Response(responseView.response_custom('Imagen eliminada',status.HTTP_200_OK,'responseok'))
            # else:
            #     return Response(responseView.response_custom(serializer.errors, status.HTTP_400_BAD_REQUEST,'responsebad'))
        else:
            return Response(responseView.response_custom('ID no encontrado', status.HTTP_400_BAD_REQUEST,'responsebad'))
