from django_filters import rest_framework as filters
from crud_api.models import Cuboid


class CuboidFilter(filters.FilterSet):
    min_length = filters.NumberFilter(field_name="length__length", lookup_expr='gte')
    max_length = filters.NumberFilter(field_name="length__length", lookup_expr='lte')
    min_width = filters.NumberFilter(field_name="width__width", lookup_expr='gte')
    max_width = filters.NumberFilter(field_name="width__width", lookup_expr='lte')
    min_height = filters.NumberFilter(field_name="height__height", lookup_expr='gte')
    max_height = filters.NumberFilter(field_name="height__height", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="area__area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="area__area", lookup_expr='lte')
    min_volume = filters.NumberFilter(field_name="volume__volume", lookup_expr='gte')
    max_volume = filters.NumberFilter(field_name="volume__volume", lookup_expr='lte')


    class Meta:
        model = Cuboid
        fields = [
        'min_length', 'max_length','min_width', 'max_width', 'min_height', 'max_height',
        'min_area', 'max_area', 'min_volume', 'max_volume'
        ]