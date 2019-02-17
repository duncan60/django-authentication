from versionInfo.models import UpdateInfo
from .serializers import UpdateInfoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class UpdateInfoViewSet(viewsets.ModelViewSet):
    queryset = UpdateInfo.objects.all()
    serializer_class = UpdateInfoSerializer

    def list(self, request):
        queryset = UpdateInfo.objects.all()
        serializer = UpdateInfoSerializer(queryset, many=True)
        return Response({
          'success': True,
          'result': serializer.data
        })

    @action(methods=['get'], detail=False)
    def newset(self, request):
        newset = self.get_queryset().order_by('id').last()
        serializer = self.get_serializer_class()(newset)
        return Response({
          'success': True,
          'result': serializer.data
        })
