from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>',views.detail,name='detail'),
    path('blog/new',views.new,name='new'),
    path('blog/create',views.create,name='create'),
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name="update"),
    path('blog/delete/<int:blog_id>', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
