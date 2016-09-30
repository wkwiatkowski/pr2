from django.contrib import admin
from .models import Author, Publisher, Book

# Register your models here.

# def. kalsy, ktora nic nie robi
#class AuthorAdmin(admin.ModelAdmin):
#    pass

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name'] # pola, ktore beda przeszukiwane
    ordering = ['last_name'] # sortowanie rosnaco, moze bys lista pol, ktore
                             # beda brane wg. podanej kolejnosci
                             # '-last_name' - malejaco

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author', 'isbn', 'publisher']
    list_display = ['title', 'author', 'isbn', 'publisher']     # def. jakie kolumny
                    # maja sie wyswietlac w module Books. wg zdef. kolumn mozna sortowac

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)

# rejestracja klas za pomca listy
#admin.site.register([Publisher, Book])

# rejestracja w ten sposob bedzie dot. modulu z pominieciem wczesniej zdef. klasy
#admin.site.register([Publisher, Book])
# lub
#admin.site.register(Book)


