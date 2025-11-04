from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .paginations import ProductPagination

from .utils import get_similar_products

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    
class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def retrieve(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        
        data = serializer.data
        
        similar_product = get_similar_products(data['id'])
        data['similar_product'] = self.serializer_class(similar_product, many= True).data
        
        return Response(data)