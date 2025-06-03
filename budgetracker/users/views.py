from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
