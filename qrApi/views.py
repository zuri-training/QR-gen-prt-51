
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from .serializers import ApiSerializer, TestSerializer
from .models import QrcodeApi
# Create your views here.

class QrcodeApiViewSet(viewsets.ModelViewSet):
    serializer_class = ApiSerializer
    queryset = QrcodeApi.objects.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

    def post(self, request):
        serializer = ApiSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
           
            return Response(
                {"status": True, "message": "Success", "Data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
           
        else:
            return Response(
                {"status": False, "message": "Error"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class TestViewSet(GenericAPIView):
    serializer_class = TestSerializer
    permission_classes=[AllowAny,]
    

    def post(self, request):
        serializer = TestSerializer(data=request.data, context={"request": request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "message": "Success", "Data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "message": "Error"},
                status=status.HTTP_400_BAD_REQUEST,
            )
