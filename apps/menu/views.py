from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.menu.filters import ProductFilter
from apps.menu.models import Article, Post, Product
from apps.menu.permissions import IsOwner
from apps.menu.serializers import ArticleSerializer, PostSerializer, ProductWriteSerializer, ProductReadSerializer


class HelloView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Hello, API!'})


class ArticleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # def get_object(self, pk):
    #     article = Article.objects.get(pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class ArticleDeleteView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwner]

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['tags__name']


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    filterset_class = ProductFilter


    def get_serializer_class(self):
        if self.action in ['post', 'create', 'update', 'partial_update']:
            return ProductWriteSerializer
        return ProductReadSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


