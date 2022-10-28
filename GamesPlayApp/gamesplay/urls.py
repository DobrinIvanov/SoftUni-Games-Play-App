from django.urls import path, include

from GamesPlayApp.gamesplay.views import index, dashboard, create_game, details_game, edit_game, delete_game, \
    create_profile, delete_profile, edit_profile, details_profile

urlpatterns = (
    path('', index, 'homepage'),
    path('dashboard/', dashboard, 'dashboard'),
    path('game/', include([
        path('create/', create_game, 'create_game'),
        path('details/<int:id>/', details_game, 'details_game'),
        path('edit/<int:id>/', edit_game, 'edit_game'),
        path('delete/<int:id>/', delete_game, 'delete_game')
    ])),
    path('profile/', include([
        path('create/', create_profile, 'create_profile'),
        path('details/', details_profile, 'details_profile'),
        path('edit/', edit_profile, 'edit_profile'),
        path('delete/', delete_profile, 'delete_profile')
    ]))
)

