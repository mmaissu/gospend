from django.urls import path
from .views import RegisterView
<<<<<<< HEAD
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
=======

urlpatterns = [
>>>>>>> e830f37d388f326c38207ee81c0965d604047d1b
    path('register/', RegisterView.as_view(), name='register'),
]
