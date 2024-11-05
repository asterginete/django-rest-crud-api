from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user operations.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    @extend_schema(
        summary="Get current user profile",
        description="Returns the profile information of the currently authenticated user",
        responses={200: UserSerializer}
    )
    @action(detail=False, methods=['get'])
    def profile(self, request):
        """Get the current user's profile information."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        summary="List all users",
        description="Returns a list of all users in the system",
        responses={200: UserSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create new user",
        description="Create a new user in the system",
        request=UserCreateSerializer,
        responses={
            201: UserSerializer,
            400: OpenApiResponse(description="Bad request")
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Get user details",
        description="Returns the details of a specific user",
        responses={
            200: UserSerializer,
            404: OpenApiResponse(description="User not found")
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Update user",
        description="Update the details of a specific user",
        request=UserSerializer,
        responses={
            200: UserSerializer,
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="User not found")
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete user",
        description="Delete a specific user from the system",
        responses={
            204: OpenApiResponse(description="User deleted successfully"),
            404: OpenApiResponse(description="User not found")
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)