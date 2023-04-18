from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from core.models import Item
from .serializer import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

# @api_view(['GET', 'PUT', 'POST'])
# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/get',
#         'GET /api/get/:id',
#         'POST /api/post',
#         'PUT /api/put',
#         'DELETE /api/delete',
#     ]
#     return Response(routes)


# @api_view(['GET'])
# def getItem(request):
#     item = Item.objects.all()
#     serializer = ItemSerializer(item, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getItems(request, pk):
#     item = Item.objects.get(id=pk)
#     serializer = ItemSerializer(item, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def post(request):
#     # item = Item.objects.get(id + 1)
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['PUT'])
# def put(request, pk):
#     product = Item.objects.get(id=pk)
#     serializer = ItemSerializer(instance=product, data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    product = Item.objects.get(id=pk)
    product.delete()

    return Response('Item Deleted Successfully !')


class ItemView(APIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        startup = Item.objects.all()
        return startup

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            print(request.query_params)
            print(id)

            if id is not None:
                startup = Item.objects.get(id=id)
                serializer = ItemSerializer(startup)
        except Exception as e:
            # print("hello")
            startups = self.get_queryset()
            serializer = ItemSerializer(startups, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        startup = Item.objects.get(id=request.query_params["id"])
        # serializer = ItemSerializer(startup)
        # if request.user.is_superuser:

        startup.delete()
        return Response({"message": "Deleted"})


class ItemInfo(APIView):
    def get(self, request, id):
        try:
            obj = Item.objects.get(id=id)

        except Item.DoesNotExist:
            msg = {"msg": "Not Found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Item.objects.get(id=id)
        except Item.DoesNotExist:
            msg = {"msg": "Not Found Error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        # data = request.data
        serializer = ItemSerializer(instance=obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
