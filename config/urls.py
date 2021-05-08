from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include('api.urls')),
    path('', include('rest_framework.urls')),

]
