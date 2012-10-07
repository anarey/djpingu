from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questions",               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    ## campos que debe mostrar el listado de objetos del modelo.
    list_display = ('question', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date'] ## Filtro vertial
    search_fields = ['question'] ## Campo de busqueda sobre el parametro
    date_hierarchy = 'pub_date'  ##  Navegacion jerarqueca en linea


admin.site.register(Poll, PollAdmin)
