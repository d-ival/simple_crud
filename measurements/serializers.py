from measurements.models import Project, Measurement
from rest_framework import serializers

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('id', 'value', 'project', 'created_at', 'updated_at')


class ProjectSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, allow_null=True,required=False)

    class Meta:
        model = Project
        fields = ('id','name', 'latitude', 'longitude', 'created_at', 'updated_at', 'measurements')
