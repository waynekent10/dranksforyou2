from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import Ingredient

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
        ingredient = Ingredient.objects.create(
           name=request.data["name"],
           image=request.data["image"]
       )
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
    def update(self, request, pk):
            ingredient = Ingredient.objects.get(pk=pk)
            ingredient.name = request.data.get("name", ingredient.name)
            ingredient.image = request.data.get("image", ingredient.image) 
            ingredient.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        

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
        fields = ['id', 'name', 'image']
        depth = 1