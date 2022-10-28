from django import forms

from CRUD.models import Book, Author, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = [
            'title',
            'quantity_received',
            'fiction',
            'category',
            'author'
        ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = [
            'name', 'surname', 'email'
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            'title'
        ]
