from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# Register the Inline class for BookInstance 
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Inline class for Book 
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


# Define and register the admin class for Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Define and register the admin class for Book Instance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('get_title', 'status', 'borrower', 'due_back', 'id')
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

    def get_title(self, book_instance):
    	return book_instance.book.title
    get_title.short_description = 'Title'# TODO: wtf is this?
    get_title.admin_order_field = 'book'

# Define and Register the Admin class for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Genre and Language Admin classes
admin.site.register(Genre)
admin.site.register(Language)
