from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostListCreateAPIView(APIView):
    def get(self, req):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = PostSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return Post.objects.filter(pk=pk).first()

    def get(self, req, pk):
        post = self.get_object(pk)
        if not post:
            return Response({"error": "Post not found"})

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, req, pk):
        post = self.get_object(pk)
        if not post:
            return Response({"error": "Post not found"})  

        serializer = PostSerializer(post, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, req, pk):
        post = self.get_object(pk)
        if not post:
            return Response({"error": "Post not found"})

        post.delete()
        return Response({"message": "Post deleted successfully"})
    
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



    

