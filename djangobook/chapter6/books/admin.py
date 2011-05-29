from django.contrib import admin
from chapter6.books.models import Publisher,Authour,Book

admin.site.register(Publisher)
admin.site.register(Authour)
admin.site.register(Book)
