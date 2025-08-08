from rest_framework import serializers

from apps.menu.models import Article, Tag, Post, Category, Product
from apps.users.models import CustomUser


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id', 'title', 'description'
        )
        # fields = ('id', 'title')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    def validate_title(self, value):
        if 'dummy' in value:
            raise serializers.ValidationError("Don't use this word for title")
        return value

    def validate(self, attrs):
        if len(attrs['title']) < 10:
            raise serializers.ValidationError("Title should be at least 10 characters long")

        return attrs


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'first_name', 'last_name'
        ]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author', 'tags'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'


class ProductWriteSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True,source='category')
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'category_id'
        ]