from django.urls import path

from apps.menu.views import HelloView, ArticleView, ArticleListView, ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('articles/', ArticleView.as_view(), name='articles'),
    # path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('articles/list/', ArticleListView.as_view(), name='articles-list'),
    path('article-create/', ArticleCreateView.as_view(), name='article-create'),
    path('article-detail/<int:pk>', ArticleDetailView.as_view(), name='article-detail')
]