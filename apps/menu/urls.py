from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.menu.views import HelloView, ArticleView, ArticleListView, ArticleCreateView, ArticleDetailView, PostListView, \
    ProductViewSet, ArticleViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('articles_2', ArticleViewSet)


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('articles/', ArticleView.as_view(), name='articles'),
    # path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('articles/list/', ArticleListView.as_view(), name='articles-list'),
    path('article-create/', ArticleCreateView.as_view(), name='article-create'),
    path('article-detail/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('post/list/', PostListView.as_view(), name='posts-list'),
    *router.urls,
]