from time import timezone

from rest_framework import permissions, views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .exceptions import MessageNotExistsException
from .models import Product, Order, OrderItem, WatchList

from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view

from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer, WatchListSerializer
from rest_framework import status
import datetime


@api_view(['GET', 'POST'])
def products_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        if request.user.is_staff:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            products = Product.objects.filter(quantity__gte=1)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid() and request.user.is_staff:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def products_detail(request, pk):
    products = Product.objects.filter(id=pk)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def orders_list(request):
    if request.method == 'GET':
        if request.user.is_staff:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            orders = Order.objects.filter(user=request.user)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        user = request.user
        new_order = Order.objects.create(user=user, order_status="Pending", date_placed=datetime.datetime.now())

        # Iterate over the items in the order
        for item in request.data.get('order', []):
            try:
                product = Product.objects.get(pk=item['productId'])
                quantity = item['quantity']
                # Check if enough quantity is available
                if product.quantity < quantity:
                    return Response(
                        {"error": "Not enough quantity available for product id {}".format(item['productId'])},
                        status=status.HTTP_400_BAD_REQUEST)
                # Create a new OrderItem instance
                OrderItem.objects.create(
                    order=new_order,
                    product=product,
                    purchased_price=product.retail_price,
                    wholesale_price=product.wholesale_price,
                    quantity=quantity
                )

                # Update product quantity
                product.quantity -= quantity
                product.save()

            except Product.DoesNotExist:
                return Response({"error": "Product id {} does not exist".format(item['productId'])},
                                status=status.HTTP_400_BAD_REQUEST)
        # Serialize the order
        serializer = OrderSerializer(new_order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def order_detail(self, request, pk):
    return Response({})



#############################################################
#############################################################
#############################################################


# class PostListCreateAPI(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class PostRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorOrReadOnly, permissions.IsAdminUser]
#
#     def perform_update(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# class CommentCreateAPI(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# class CommentRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     def perform_update(self, serializer):
#         serializer.save(author=self.request.user)


class MessageApi(views.APIView):
    def get(self, request, *args, **kwargs):
        # return Response({'message': 'Hello, world!'})
        raise MessageNotExistsException

    def post(self, request, *args, **kwargs):
        return Response({'message': request.data["message"], 'data': request.data["data"]})
