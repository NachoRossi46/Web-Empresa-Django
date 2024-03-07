from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'uptated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'uptated') # Campos de solo lectura
    list_display = ('title', 'author', 'published', 'post_categories') # Campos a mostrar
    ordering = ('author', 'published') # Ordenar primero por autor y luego por fecha de publicación
    search_fields = ('title', 'content', 'author__username', 'categories__name') # Campos de búsqueda por los diferentes campos
    date_hierarchy = 'published' # Jerarquía de fechas
    list_filter = ('author__username', 'categories__name') # Filtros
    
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')]) # Concatenar las categorías de la entrada
    post_categories.short_description = 'Categorías' # Nombre de la columna
   
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
