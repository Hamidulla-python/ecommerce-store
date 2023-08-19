from rest_framework import serializers
from .models import Product, Review, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = '__all__'


class PorductSerializers(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'avg_rating']
