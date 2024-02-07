from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static,settings

urlpatterns = [
    re_path('^admin/', admin.site.urls, name="admin_login"),
    path('', include("grade.urls")),
    path('', include("homepage.urls")),
     path("__debug__/", include("debug_toolbar.urls")),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
