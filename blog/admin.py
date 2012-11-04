from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from blog.models import Category, Post, Tag, PostImage

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title',)

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

#class TagAdmin(admin.ModelAdmin):
#    pass

class PostImageAdmin(admin.ModelAdmin):
    pass


#
#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'email')
#    search_fields = ('first_name', 'last_name')
#
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'publisher', 'publication_date')
#    list_filter = ('publication_date',)
#    date_hierarchy = 'publication_date'
#    ordering = ('-publication_date',)
#    filter_horizontal = ('authors',)
#    raw_id_fields = ('publisher',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(Tag, TagAdmin)
admin.site.register(PostImage, PostImageAdmin)
