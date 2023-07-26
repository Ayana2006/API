from rest_framework import viewsets
from apps.posts.models import Post, Comment, Like, LikeComments
from apps.posts.serializers import PostSerializer, CommentSerializer, LikeSerializer, LikeCommentsSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
class LikeCommentsViewSet(viewsets.ModelViewSet):
    queryset = LikeComments.objects.all()
    serializer_class = LikeCommentsSerializer
# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostDestroyAPIVIew(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer 