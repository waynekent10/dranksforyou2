from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from dranksforyou2api.models import Beverage

class BeverageView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single beverage"""
        try:
            beverage = Beverage.objects.get(pk=pk)
            serializer = BeverageSerializer(beverage, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Beverage.DoesNotExist:
            return Response({'message': 'Beverage not found'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests for all beverages"""
        beverages = Beverage.objects.all()
        serializer = BeverageSerializer(beverages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests to create a new beverage"""
        try:
            beverage = Beverage.objects.create(
                name=request.data["name"],
                liquor_id=request.data["liquor_id"],
                ingredient_id=request.data["ingredient_id"],
                description=request.data["description"],
                price=request.data["price"],
                image=request.data["image"],
            )
            serializer = BeverageSerializer(beverage)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        """Handle PUT requests to update a beverage"""
        try:
            beverage = Beverage.objects.get(pk=pk)
            beverage.name = request.data.get("name", beverage.name)
            beverage.liquor_id = request.data.get("liquor_id", beverage.liquor_id)
            beverage.ingredient_id = request.data.get("ingredient_id", beverage.ingredient_id)
            beverage.description = request.data.get("description", beverage.description)
            beverage.price = request.data.get("price", beverage.price)
            beverage.image = request.data["image", beverage.image]
            beverage.save()

            serializer = BeverageSerializer(beverage)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Beverage.DoesNotExist:
            return Response({'message': 'Beverage not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a beverage"""
        try:
            beverage = Beverage.objects.get(pk=pk)
            beverage.delete()
            return Response({'message': 'Beverage deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Beverage.DoesNotExist:
            return Response({'message': 'Beverage not found'}, status=status.HTTP_404_NOT_FOUND)

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = ['id', 'name', 'ingredient_id', 'liquor_id', 'description', 'price', 'image']
        depth = 2
