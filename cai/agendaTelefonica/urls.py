from django.urls import path
from . import views

urlpatterns = [
    path('', views.persona_list, name='persona_list'),
    path('view/<int:pk>', views.persona_view, name='persona_view'),
    path('new', views.persona_create, name='persona_new'),
    path('edit/<int:pk>', views.persona_update, name='persona_edit'),
    path('delete/<int:pk>', views.persona_delete, name='persona_delete'),
]