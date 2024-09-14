from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import User

class UserView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests to create a new user"""
        user = User.objects.create(
            name=request.data["name"],
            username=request.data["username"],
            email=request.data["email"],
            admin=request.data.get("admin", False),
            uid=request.data["uid"]
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT/PATCH requests to update an existing user"""
        try:
            user = User.objects.get(pk=pk)
            user.name = request.data.get("name", user.name)
            user.username = request.data.get("username", user.username)
            user.email = request.data.get("email", user.email)
            user.admin = request.data.get("admin", user.admin)
            user.uid = request.data.get("uid", user.uid)
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a user"""
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'uid', 'id', 'admin']
        depth = 1