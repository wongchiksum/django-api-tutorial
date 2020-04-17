from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t1/', include('tutorial1.urls')),
    path('t2/', include('tutorial2.urls')),
    path('t3/', include('tutorial3.urls')),
    path('t4/', include('tutorial4.urls')),
    path('t5/', include('tutorial5.urls')),
    path('t6/', include('tutorial6.urls')),
    path('api/upload/', include('f_file.urls')),
    path('api/app/', include('a_shop.urls')),
    path('api/function/', include('f_system_log.urls')),
    re_path(r'^((?!media).)*$', TemplateView.as_view(template_name="index.html"))
]

# Files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
