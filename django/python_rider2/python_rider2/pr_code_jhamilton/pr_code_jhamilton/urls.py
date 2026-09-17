from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('code-jhamilton/', include('app_codejhamilton.urls')),
]