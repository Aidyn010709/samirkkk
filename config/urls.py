"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API made with love <3",
      default_version='v1',
      description="Contacts: tg @Backspyz, phone: +996707608037",
      contact=openapi.Contact(email="samirkk@gmail.com"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('account/', include('applications.account.urls')),
    path('apartment/', include('applications.apartment.urls')),
    path('order/', include('applications.order.urls')),
    path('spam/', include('applications.spam.urls')),
    path('help-center/', include('applications.helpcenter.urls')),
    path('giftcard/', include('applications.giftcard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
