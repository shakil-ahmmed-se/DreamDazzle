from rest_framework.routers import DefaultRouter
from .import views 
from django.urls import path, include

router = DefaultRouter()
router.register('list', views.UserViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('register/', views.RegistrationApiView.as_view(), name='register'),
    path('login/', views.LoginApiView.as_view(), name='login')
]
