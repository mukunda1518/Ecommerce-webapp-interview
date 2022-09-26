from rest_framework import serializers
from .models import Product, Color


class ProductSerializer(serializers.ModelSerializer):

    colors_list = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_colors_list(self, instance):
        colors = []
        colors_objs = instance.color_set.all()
        for obj in colors_objs:
            colors.append(obj.name)
        return colors


class ColorSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Color
        fields = "__all__"
