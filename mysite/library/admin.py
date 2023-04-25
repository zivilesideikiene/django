from django.contrib import admin
from . import models

class BookInstanceInLine(admin.TabularInline):
    model = models.BookInstance
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "isbn", "author", "display_genre"]   #nustatom, kaip sarasas bus atvaizduojamas
    inlines = [BookInstanceInLine]
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["book", "uuid", "status", "due_back"]
    list_filter = ['status', 'due_back', 'book']

    fieldsets = (
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookInstance, BookInstanceAdmin)

