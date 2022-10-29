from django.urls import path, include

from GamesPlayApp.gamesplay.views import index, dashboard, create_game, details_game, edit_game, delete_game, \
    create_profile, delete_profile, edit_profile, details_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', create_game, name='create_game'),
        path('details/<int:id>/', details_game, name='details_game'),
        path('edit/<int:id>/', edit_game, name='edit_game'),
        path('delete/<int:id>/', delete_game, name='delete_game')
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create_profile'),
        path('details/', details_profile, name='details_profile'),
        path('edit/', edit_profile, name='edit_profile'),
        path('delete/', delete_profile, name='delete_profile')
    ])),
)

