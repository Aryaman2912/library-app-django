from django.contrib import admin
from .models import Book,BookInstance,Genre,Language,Author

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInstanceInLine(admin.TabularInline):
    model=BookInstance
    extra = 0

class BookInLine(admin.TabularInline):
    model=Book
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines=[BookInstanceInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status','due_back')

    fieldsets = (
        (None,{'fields':('book','imprint','id')}),
        ('Availabilty',{'fields':('status','due_back')}),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
    inlines = [BookInLine]