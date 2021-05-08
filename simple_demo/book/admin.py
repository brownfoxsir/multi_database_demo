from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportMixin
from import_export.resources import ModelResource
from .models import Book


class BookResource(ModelResource):
    class Meta:
        model = Book
        exclude = ('id',)
        import_id_fields =('name',)


class BookAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = BookResource


admin.site.register(Book, BookAdmin)