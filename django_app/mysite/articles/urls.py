from django.urls import path

from . import views

urlpatterns = [
	# ex: /article/
    path('', views.index, name='index'),
    # ex: /article/5/
    path('<int:article_id>/', views.detail, name='detail'),
    # ex: /article/5/results/
    path('<int:article_id>/results/', views.results, name='results'),
]

