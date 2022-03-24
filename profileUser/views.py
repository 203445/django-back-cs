import json
from multiprocessing import context
from operator import or_
import re
from traceback import print_tb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from primerComponente.views import responseView
from django.contrib.auth.models import User

#importanciones necesarias
from posixpath import split
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.conf import settings
import os


# Create your views here.
# Importación de modelos
from profileUser.models import Profileimage

# Importación de serializers
from profileUser.serializers import terceraTablaSerializers
from registro.serializers import UpdateUserSerializer, RegisterSerializerNew

# Create your views here.



class PrimerViewList(APIView):

    def get(self, request, format=None):
        info = Profileimage.objects.all()
        serializer = terceraTablaSerializers(info,many=True ,context={'request':request})
        return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))

  
    def post(self, request, format=None):
        serializer = terceraTablaSerializers(data = request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()

            return Response(responseView.response_custom(serializer.data,status.HTTP_201_CREATED,'responseok'))
        else:
            return Response(responseView.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'responsebad'))

class PrimerViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Profileimage.objects.get(pk = pk)
        except Profileimage.DoesNotExist:
            return 404

    def get_objectUser(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            return 404


    def get(self, request, pk, format=None):
        responsU = self.get_objectUser(pk)
        if responsU != 404:

            serializer2 = UpdateUserSerializer(responsU, context={'request': request})
            respt = self.get_object(pk)

            if respt != 404:
                serializer = terceraTablaSerializers(respt, context={'request': request})

                answ = json.dumps(serializer2.data)
                answ = json.loads(answ)
                answ.update({"url_img":serializer.data.__getitem__("url_img"),"id_user": serializer.data.__getitem__("id_user")})
                print(answ)
                return Response(answ)
            else:
                answ = json.dumps(serializer2.data)
                answ = json.loads(answ)
                answ.update({"url_img": None})
                print(answ)
                return Response(answ)
        else:
            return Response(responseView.response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST,'responsebad'))

    def put(self, request, pk, format=None):
        responsU = self.get_objectUser(pk)
        respt = self.get_object(pk)
        if responsU != 404 :

            serializer2 = UpdateUserSerializer(responsU, data = request.data, context={'request': request})
            if serializer2.is_valid():
                
                serializer2.save()
                
                if  respt != 404:

                    serializer = terceraTablaSerializers(respt, data = request.data ,context={'request': request})

                    if serializer.is_valid():

                        if "url_img" in request.data:
                            fotos = get_object_or_404(Profileimage, pk = pk)
                            partes = (fotos.url_img.url).split("/")
                            ratok = "\\" +str(partes[2])+ "\\"+ str(partes[3])
                            os.remove(os.path.join(settings.MEDIA_ROOT  + ratok))
                
                        serializer.save()
                    return Response(responseView.response_custom(serializer.data,status.HTTP_200_OK,'responseok'))

                return Response(responseView.response_custom(serializer2.data,status.HTTP_200_OK,'responseok'))
            else:
                return Response(responseView.response_custom("Error",status.HTTP_400_BAD_REQUEST,'responsebad'))
        else:
            return Response(responseView.response_custom('ID no encontrado',status.HTTP_400_BAD_REQUEST,'responsebad'))

    def delete (self, request, pk, format=None):
        respons = self.get_object(pk)
        if respons !=404:
            fotos = get_object_or_404(Profileimage, pk = pk)
            partes = (fotos.url_img.url).split("/")
            ratok = "\\" +str(partes[2])+ "\\"+ str(partes[3])
            os.remove(os.path.join(settings.MEDIA_ROOT  + ratok))
          
            fotos.delete()
            respons.delete()
            return Response(responseView.response_custom('Dato eliminado',status.HTTP_200_OK,'responseok'))
        else:
            return Response(responseView.response_custom('ID no encontrado', status.HTTP_400_BAD_REQUEST,'responsebad'))
