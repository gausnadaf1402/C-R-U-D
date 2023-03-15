from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('show',views.show,name='show'),
    path('send',views.send,name='send'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('recordedit',views.recordedit,name='recordedit'),
]