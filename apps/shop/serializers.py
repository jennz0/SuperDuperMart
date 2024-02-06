from rest_framework import serializers

from apps.shop.models import Product, Order, OrderItem, WatchList


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'

# class PostSerializer(serializers.ModelSerializer):
#
#     comments = serializers.SerializerMethodField()
#
#     def get_comments(self, obj):
#         comments = Comment.objects.filter(post=obj)
#         return CommentSerializer(comments, many=True).data
#
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
