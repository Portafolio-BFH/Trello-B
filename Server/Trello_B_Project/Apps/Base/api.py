from rest_framework import generics, status
from rest_framework.response import Response

class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state = True)
    
class GeneralCreateAPIView(generics.CreateAPIView):
    serializer_class = None
    message_success = ''

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GeneralRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = None

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

class GeneralDestroyAPIView(generics.DestroyAPIView):
    serializer_class = None
    message_success = ''
    message_notfound = ''

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def delete(self, request, pk=None):
        entity = self.get_queryset().filter(id = pk).first()
        if entity:
            entity.state = False
            entity.save()
            return Response({'message': self.message_success}, status=status.HTTP_200_OK)
        return Response({'error': self.message_notfound}, status=status.HTTP_404_NOT_FOUND)