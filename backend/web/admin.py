from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)#都好不要删，要传列表

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ("author",)