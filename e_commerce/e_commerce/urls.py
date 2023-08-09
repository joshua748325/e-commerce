from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('item/',include('item.urls',namespace="item")),
    path('dashboard/',include('dashboard.urls',namespace="dashboard")),
    path('inbox/',include('conversation.urls',namespace="conversation")),
    path('accounts/',include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # To access files in media folder as static (only safe for development mode)

handler403='e_commerce.views.custom_403_view'
handler404='e_commerce.views.custom_404_view'
handler500='e_commerce.views.custom_500_view'