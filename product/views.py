from django.shortcuts import render

from rest_framework import viewsets
#Authentication Token and Login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import (
                    SessionAuthentication, 
                    BasicAuthentication, 
                    TokenAuthentication)


from .serializers import ProductSerializer
from .models import Product

#classe para filtrar , serializar e solitar autentificação por login ou token
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('productName')
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


