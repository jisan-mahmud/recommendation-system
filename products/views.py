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
        serializer = self.get_serializer
        
        data = serializer(self.get_object()).data
        data.pop('url')
        
        similar_products = get_similar_products(data['id'])
        data['similar_products'] = serializer(similar_products, many= True).data
        
        return Response(data)