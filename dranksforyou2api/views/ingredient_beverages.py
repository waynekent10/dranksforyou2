from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou1api.models import IngredientBeverage, Beverage, Ingredient


class IngredientBeverageView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            ingredient_beverage = IngredientBeverage.objects.get(pk=pk)
            serializer = IngredientBeverageSerializer(ingredient_beverage)
            return Response(serializer.data)
        except IngredientBeverage.DoesNotExist:
            return Response({'message': 'ingredient beverage not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def list (self, request):
            ingredient_beverages=IngredientBeverage.objects.all()
            serializer = IngredientBeverageSerializer(ingredient_beverages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self, request):
            ingredient = Ingredient.objects.get(pk=request.data["ingredient"])
            beverage = Beverage.objects.get(pk=request.data['beverage'])
            
            ingredient_beverage = IngredientBeverage.objects.create(
                ingredient= ingredient,
                beverage = beverage
            )
            
            serializer = IngredientBeverageSerializer(ingredient_beverage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destroy(self, request, pk):
        try:
            ingredient_beverage = IngredientBeverage.objects.get(pk=pk)
            ingredient_beverage.delete()
            return Response({'message': 'IngredientBeverage deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except IngredientBeverage.DoesNotExist:
            return Response({'message': 'IngredientBeverage not found'}, status=status.HTTP_404_NOT_FOUND)
        
class IngredientBeverageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IngredientBeverage
        fields = ('id', 'ingredient', 'beverage')
        depth = 1
            
