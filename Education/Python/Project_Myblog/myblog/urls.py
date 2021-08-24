from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('accounts/', include('django.contrib.auth.urls')),
    url('favicon.ico', RedirectView.as_view(url='/static/myblog/img/favicon.ico'), name='favicon'),
    url('register/', views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)