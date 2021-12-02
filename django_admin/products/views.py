from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from products.producer import publish
from .models import Product, User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data)
    
class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        user= random.choice(users)
        return Response({
            'id': user.id
        })