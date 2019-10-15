from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework import status
# from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProductView(APIView):

    def get(self, request, prod_id):
        db_prod = Product.objects.get(id=prod_id)
        if db_prod or db_prod is not None:
            serializer = ProductSerializer(db_prod)
            return Response({
                "Status": "200",
                "product": serializer.data
            })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    def post(self, request):
        product = request.data.get("product")
        serializer = ProductSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Status": "200",
                "message": "Product created successfully!"
            })
        else:
            return Response({
                "Status": "400",
                "message": "Invalid Request!"
            })

    def put(self, request, prod_id):
        db_prod = Product.objects.get(id=prod_id)
        if db_prod or db_prod is not None:
            new_prod = request.data.get('product')
            serializer = ProductSerializer(instance=db_prod, data=new_prod)
            if serializer.is_valid():
                product_updated = serializer.save()
                return Response({
                    "Status": "202",
                    "product": serializer.data,
                    "Message": "Product " + serializer.data.get('ProductCode') + " has been updated!"
                })
            else:
                return Response({
                    "Status": "400",
                    "Message": "Invalid Request!"
                })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    def delete(self, request, prod_id):
        product = Product.objects.get(id=prod_id)
        if product or product is not None:
            product.delete()
            return Response({
                'success': "200",
                'message': "Product successfuly deleted"})

class ShowProduct(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            "Status": "200",
            "products": serializer.data
        })

class CategoryView(APIView):

    def get(self, request, cat_id):
        db_cat = Category.objects.get(id=cat_id)
        if db_cat or db_cat is not None:
            serializer = CategorySerializer(db_cat)
            return Response({
                "Status": "200",
                "Category": serializer.data
            })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    def post(self, request):
        category = request.data.get("Category")
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Status": "200",
                "message": "Category created successfully!"
            })
        else:
            return Response({
                "Status": "400",
                "message": "Invalid Request!"
            })

    def put(self, request, cat_id):
        db_cat = Category.objects.get(id=cat_id)
        if db_cat or db_cat is not None:
            new_cat = request.data.get('Category')
            serializer = CategorySerializer(instance=db_cat, data=new_cat)
            if serializer.is_valid():
                Category_updated = serializer.save()
                return Response({
                    "Status": "202",
                    "Category": serializer.data,
                    "Message": "Category has been updated!"
                })
            else:
                return Response({
                    "Status": "400",
                    "Message": "Invalid Request!"
                })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    def delete(self, request, cat_id):
        category = Category.objects.get(id=cat_id)
        if category or category is not None:
            category.delete()
            return Response({
                'success': "200",
                'message': "Category successfuly deleted"})

class ShowCategory(APIView):

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({
            "Status": "200",
            "Categories": serializer.data
        })

class CategoryProductView(APIView):

    def get(self, request, cat_id):
        db_relation = CategoryProduct.objects.filter(CategoryID=cat_id).all()
        if db_relation or db_relation is not None:
            serializer = CategoryProductSerializer(db_relation, many=True)
            return Response({
                "Status": "200",
                "relation": serializer.data
            })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    def post(self, request):
        relation = request.data.get("relation")
        serializer = CategoryProductSerializer(data=relation)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Status": "200",
                "message": "relation created successfully!"
            })
        else:
            return Response({
                "Status": "400",
                "message": "Invalid Request!"
            })

    def delete(self, request, cat_id):
        db_relation = CategoryProduct.objects.filter(CategoryID=cat_id).all()
        if db_relation or db_relation is not None:
            for relation in db_relation:
                relation.delete()
            return Response({
                'success': "200",
                'message': "Category successfuly deleted"
                })
