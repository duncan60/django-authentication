from rest_framework import serializers
from versionInfo.models import Draft, UpdateInfo


class DraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Draft
        fields = ('platform', 'version', 'update_text', 'force_update',
                  'pub_date')


class UpdateInfoSerializer(serializers.HyperlinkedModelSerializer):

    info = DraftSerializer(required=True)

    class Meta:
        model = UpdateInfo
        fields = ('id', 'info')
