from django.contrib import admin
from clients.models import User, Game
from django.utils.html import format_html


class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'last_name', 'username', 'email', 'password', 'about_me', 'is_staff', 'is_active', 'profile_pic')
    list_display = ('name', 'last_name', 'username')

    class Meta:
        model = User


class GameAdmin(admin.ModelAdmin):
    list_display = ('thumb', 'name_game', 'release_year')

    def thumb(self, obj):
        return format_html(f'<img src="{obj.game_img.url}" alt="" width="32px">')


admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)

