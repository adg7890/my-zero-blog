from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bloh.urls')),
    path('accounts/', include('accounts.urls')),
]
