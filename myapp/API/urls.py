from django.urls import path,include
from myapp.API import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('crud',views.api1)

urlpatterns = [
    path('',include(router.urls)),
    ]
