from rest_framework import generics
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 