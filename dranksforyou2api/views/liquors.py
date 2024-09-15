from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import Liquor

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
        liquor = Liquor.objects.create(
           name=request.data["name"],
           image=request.data["image"],
           uid=request.user
       )
        serializer = LiquorSerializer(liquor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
    def update(self, request, pk):
        """Handle PUT requests to update a liquor"""
        try:
            liquor = Liquor.objects.get(pk=pk)
            if liquor.uid != request.user:
                return Response({'message': 'You do not have permission to delete this beverage'}, status=status.HTTP_403_FORBIDDEN)
            
            liquor.name = request.data.get("name", liquor.name)
            liquor.image = request.data.get("image", liquor.image)
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
            if liquor.uid != request.user:
                return Response({'message': 'You do not have permission to delete this beverage'}, status=status.HTTP_403_FORBIDDEN)
            
            liquor.delete()
            return Response({'message': 'Liquor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Liquor.DoesNotExist:
            return Response({'message': 'Liquor not found'}, status=status.HTTP_404_NOT_FOUND)
   
class LiquorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquor
        fields = ['id', 'name', 'image', 'uid']
        depth = 1