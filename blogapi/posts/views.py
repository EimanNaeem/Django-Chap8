from rest_framework import generics #, permissions
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerailizer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerailizer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,) #new
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerailizer
