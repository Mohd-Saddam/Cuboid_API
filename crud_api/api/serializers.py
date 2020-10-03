from rest_framework import serializers
from crud_api.models import (Cuboid,FilterLength,FilterWidth,FilterHeight,
    FilterArea,FilterVolume)

class CuboidSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='cuboid_delete_api', lookup_field='pk')
    length = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    class Meta:
        model = Cuboid
        fields = [
            'url', 'id', 'title', 'length','width','height','area','volume','status'
        ]

    def get_length(self, obj):
        return obj.get_length()
    def get_width(self, obj):
        return obj.get_width()
    def get_height(self, obj):
        return obj.get_height()
    def get_area(self,obj):
        return  obj.get_area()
    def get_volume(self,obj):
        return  obj.get_volume()


class CuboidCreateSerializers(serializers.ModelSerializer):
    def validate_created_by(self, created_by):
        max_count = 100
        created_count = Cuboid.objects.filter(created_by=self.context['request'].user).count()
        if created_count >= max_count:
            raise serializers.ValidationError("User allowed to create maximum of %s items" % max_count)
        return created_by

    class Meta:
        model = Cuboid
        fields = "__all__"
        


class CuboidUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuboid
        fields = [
            'title', 'length','width','height','area','volume',
        ]


# class CuboidCreatorSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='staff_cuboid_detail_api', lookup_field='pk')
#     created_by = serializers.SerializerMethodField()
#     staff_product = CuboidSerializer(many=True)
#     class Meta:
#         model = Creator
#         fields = [
#             "url", "id", "created_by", "staff_product"
#         ]

#     def get_created_by(self,obj):
#         return  obj.get_fullname()