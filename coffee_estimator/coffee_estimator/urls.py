from django.urls import path
from django.contrib import admin
from ml_model import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_coffee, name='create_coffee'),
    path('success/', views.success_page, name='success_page'),  # Add a URL for the success page
    path('tutorial/', views.tutorial, name='tutorial'),
        # Add a URL for the success page
    # Add other URL patterns as needed
]
