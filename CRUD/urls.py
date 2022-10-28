from django.urls import path

from CRUD.views import IndexView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, CategoryDetailView, \
    CategoryUpdateView, CategoryDeleteView, AuthorDetailView, AuthorUpdateView, AuthorDeleteView, AuthorCreateView, \
    CategoryCreateView, BookListView, CategoryListView, AuthorListView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('books/create/', BookCreateView.as_view(), name='create-new-book'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='delete-book'),
    path('books/list/', BookListView.as_view(), name='book-list'),


    path('category/detail/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),
    path('category/create/', CategoryCreateView.as_view(), name='create-category'),
    path('category/list/', CategoryListView.as_view(), name='category-list'),

    path('author/detail/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='author-delete'),
    path('author/create/', AuthorCreateView.as_view(), name='create-author'),
    path('author/list/', AuthorListView.as_view(), name='author-list'),

]
