from rest_framework import generics, viewsets
from apps.posts.models import Post, Comment
from apps.posts.serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostDestroyAPIVIew(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer 