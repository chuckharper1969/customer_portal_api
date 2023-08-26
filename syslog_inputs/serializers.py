from rest_framework import serializers
from syslog_inputs.models import SyslogInput
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='sysloginput-detail',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'owner']


class SyslogInputSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = SyslogInput
        fields = ['id', 'input_id', 'udp_port', 'tcp_port', 'message', 'status', 'owner', 'created_at']

    def create(self, validated_data):
        return SyslogInput.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.input_id = validated_data.get('input_id', instance.input_id)
        instance.udp_port = validated_data.get('udp_port', instance.udp_port)
        instance.tcp_port = validated_data.get('tcp_port', instance.tcp_port)
        instance.message = validated_data.get('message', instance.message)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
