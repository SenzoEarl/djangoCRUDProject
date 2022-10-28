from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from CRUD.forms import BookForm
from CRUD.models import Book, Category, Author


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book-list.html'


class BookCreateView(CreateView):
    template_name = 'books/book-create.html'
    model = Book
    fields = [
        'title',
        'quantity_received',
        'fiction',
        'category',
        'author'
    ]

    success_url = reverse_lazy('book-list')


class BookDetailView(DetailView):
    template_name = 'books/book-detail.html'
    model = Book


class BookUpdateView(UpdateView):
    template_name = 'books/book-update.html'
    model = Book
    fields = [
        'title',
        'quantity_received',
        'fiction',
        'category',
        'author'
    ]

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.id})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('book-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category-list.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/category-create.html'
    fields = [
        'title'
    ]
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    template_name = 'category/category-update.html'
    model = Category
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('category-detail', kwargs={'pk': self.object.id})


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category-delete.html'
    success_url = reverse_lazy('category-list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category-detail.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author-list.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'authors/author-create.html'
    fields = [
        'name', 'surname', 'email'
    ]
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'surname', 'email']

    def get_success_url(self):
        return reverse_lazy('author-detail', kwargs={'pk': self.object.id})


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/author-delete.html'
    success_url = reverse_lazy('author-list')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author-detail.html'
