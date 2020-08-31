from django.urls import path
from .views import profile, register_game, update_game, delete_game
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', profile, name='profile'),
    path('cadastro', register_game, name='register_game'),
    path('update/<int:id>/', update_game, name='update_game'),
    path('delete/<int:id>/', delete_game, name='delete_game'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)