from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from recipe import views

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeView, 'recipe')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
