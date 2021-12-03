from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from products.producer import publish
from .models import Product, User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects
    serializer_class = ProductSerializer
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        if product is not None:
            product.delete()
            publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        user= random.choice(users)
        return Response({
            'id': user.id
        })