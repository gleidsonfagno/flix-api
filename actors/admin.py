from django.contrib import admin
from actors.models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    # os cmopos que queremos mostrar no admin
    list_display = ("id", "name", "birthday", "natinality")
