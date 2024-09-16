from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import Ingredient, User

class IngredientView(ViewSet):
    def retrieve(self,request, pk):
        """Handle GET requests for single ingredient

        Returns:
            Response -- JSON serialized ingredient
        """
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            serializer = IngredientSerializer(ingredient, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist as ex:
            return Response({'Ingredient does not exist': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request): 
        """Handle GET requests to get all ingredients

        Returns:
            Response -- JSON serialized list of ingredients
        """
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST operations"""
        user = User.objects.get(pk=request.data['user_id'])
        ingredient = Ingredient.objects.create(
            user =user,
            name=request.data["name"],
       )
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
    def update(self, request, pk):
            
        """Handle PUT requests to update an ingredient"""
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            user = User.objects.get(pk=request.data['user_id'])
            ingredient.user = user
            ingredient.name = request.data.get("name", ingredient.name)
            ingredient.save()

            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist:
            return Response({'message': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def destroy(self, request, pk):
        """Handle DELETE requests to delete an ingredient"""
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.delete()
            return Response({'message': 'Ingredient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist:
            return Response({'message': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)
   
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'user']
        depth = 1