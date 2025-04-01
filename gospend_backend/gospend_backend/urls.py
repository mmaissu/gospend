from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # <-- Добавляем админку
    path("api/", include("users.urls")),  # <-- API (если у тебя есть)
]
