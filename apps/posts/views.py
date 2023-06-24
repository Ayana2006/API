from rest_framework import generics, viewsets
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
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