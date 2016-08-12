from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from serializers import ClientSerializer
from models import AiklagUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from permissions import IsCreationOrIsAuthenticated


class ClientViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = AiklagUser.objects.all()
    serializer_class = ClientSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsCreationOrIsAuthenticated, ]

    def get(self, request):
        serializer = AiklagUser(request.user)
        return Response(serializer.data)

    def create(self, request):
        serialized = ClientSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):

        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
