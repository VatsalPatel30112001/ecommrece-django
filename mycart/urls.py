from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('shop/',include('shop.urls')),
    path('blog/',include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
