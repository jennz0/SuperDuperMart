from rest_framework import permissions, views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .exceptions import MessageNotExistsException
from .models import Post, Comment

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostListCreateAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateAPI(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class MessageApi(views.APIView):
    def get(self, request, *args, **kwargs):
        # return Response({'message': 'Hello, world!'})
        raise MessageNotExistsException

    def post(self, request, *args, **kwargs):
        return Response({'message': request.data["message"], 'data': request.data["data"]})
