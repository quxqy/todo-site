
from django.contrib import admin
from django.urls import path
from tasks.views import *
from django.contrib.auth import views as authViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('add/', add_task, name='add_task'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('register/',register, name='register'),
    path('',login, name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/<int:user_id>/',profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
