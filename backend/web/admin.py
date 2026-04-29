from django.contrib import admin
from web.models.user import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)#都好不要删，要传列表
    