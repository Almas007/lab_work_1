from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('categories/<int:id>/products', views.categories_list),
]

urlpatterns += router.urls

# urlpatterns = router.urls
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('category/<int:category_id>/', views.categories_list, name='category')
# ]