from django.http import Http404
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializer import ProductSerializer


class ProductsList(APIView, LimitOffsetPagination):

    def get(self, request):
        products = Product.objects.all()
        results = self.paginate_queryset(products, request, view=self)
        serializers = ProductSerializer(results, many=True)
        return self.get_paginated_response(serializers.data)


class ProductDetails(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)
