from django.contrib import admin
from chapter7.books.models import Publisher,Authour,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("firstName","lastName","email")
    search_fields = ("firstName","lastName")

class BookAdmin(admin.ModelAdmin):
    list_display =("title","publisher","publicationDate")
    list_filter = ("publicationDate",)
    date_hierarchy = "publicationDate"
    ordering = ("-publicationDate",)
    filter_horizontal = ("authors",)
    raw_id_fields = ("publisher",)

admin.site.register(Publisher)
admin.site.register(Authour,AuthorAdmin)
admin.site.register(Book,BookAdmin)
