from django.shortcuts import render
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

