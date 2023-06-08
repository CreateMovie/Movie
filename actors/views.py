from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Movie
from django.views.generic import ListView, DetailView


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"