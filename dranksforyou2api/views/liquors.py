from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import Liquor, User

class LiquorView(ViewSet):
    def retrieve(self,request, pk):
        try:
            liquor = Liquor.objects.get(pk=pk)
            serializer = LiquorSerializer(liquor, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Liquor.DoesNotExist as ex:
            return Response({'Liquor does not exist': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request): 
        liquors = Liquor.objects.all()
        serializer = LiquorSerializer(liquors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST operations"""
        user = User.objects.get(pk=request.data['user_id'])
        liquor = Liquor.objects.create(
           user =user,
           name=request.data["name"],
       )
        serializer = LiquorSerializer(liquor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
    def update(self, request, pk):
        """Handle PUT requests to update a liquor"""
        try:
            liquor = Liquor.objects.get(pk=pk)
            user = User.objects.get(pk=request.data['user_id'])
            liquor.user = user
            liquor.name = request.data.get("name", liquor.name)
            liquor.save()

            serializer = LiquorSerializer(liquor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Liquor.DoesNotExist:
            return Response({'message': 'Liquor not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a liquor"""
        try:
            liquor = Liquor.objects.get(pk=pk)
            liquor.delete()
            return Response({'message': 'Liquor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Liquor.DoesNotExist:
            return Response({'message': 'Liquor not found'}, status=status.HTTP_404_NOT_FOUND)
   
class LiquorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquor
        fields = ['id', 'name', 'user']
        depth = 1