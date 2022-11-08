from django.contrib.auth import login
from issues.models import Issue
from issues.serializers import IssueSerializer, LoginSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import View
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class IssueModelViewSet(ModelViewSet):

    model = Issue
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class AuthView(GenericViewSet):

    serializer_class = LoginSerializer

    @action(detail=False, serializer_class=LoginSerializer, methods=["post"])
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({"details": "You successfully logged in"})

    @action(detail=False, serializer_class=None)
    def logout(self):
        return Response({"details": "You successfully logged out"})
