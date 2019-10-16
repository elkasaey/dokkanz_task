from django.urls import path
from django.conf.urls import include
from . views import *
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path("Products/", ProductView.as_view()),
    path('Products/<prod_id>', ProductView.as_view()),
    path('Products/show/all', ShowProduct.as_view()),

    path("relation/", CategoryProductView.as_view()),
    path('relation/<cat_id>', CategoryProductView.as_view()),

    path("Category/", CategoryView.as_view()),
    path('Category/<cat_id>', CategoryView.as_view()),
    path('Category/show/all', ShowCategory.as_view()),

    # path("swagger", schema_view)
    # path('', include('swagger_ui.urls')),

]
