from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse as api_reverse
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .filters import (CuboidFilter)
from .permissions import (IsAuthenticated, IsStaff, IsOwner)
from .serializers import (CuboidSerializer, 
	CuboidCreateSerializers, CuboidUpdateSerializers)
from crud_api.models import (Cuboid,FilterLength,FilterWidth,
	FilterHeight,FilterArea,FilterVolume)



class APIHomeView(APIView):
	def get(self, request, format=None):
		data = {
			"cuboid_filterlist_page": {
				"filter_list_API":  api_reverse("cuboid_list_api", request=request),
			},
			"cuboid_CRUD_page": {
				"cuboid_create_API":  api_reverse("cuboid_create_api", request=request),
				# "cuboid_update_API":  api_reverse("cuboid_update_api", request=request),
				# "cuboid_delete_API":  api_reverse("cuboid_delete_api", request=request),
			},

		}
		return Response(data)


# class StaffCuboidListApiView(generics.ListAPIView):
#     model = Creator
#     queryset = Creator.objects.all()
#     serializer_class = CuboidCreatorSerializer
#     permission_classes = [IsStaff]
#     # filter_backends = [
#     #     DjangoFilterBackend,
#     # ]
#     # filterset_class = CuboidFilter


# class StaffCuboidDetailApiView(generics.RetrieveAPIView):
#     model = Creator
#     queryset = Creator.objects.all()
#     serializer_class = CuboidCreatorSerializer
#     permission_classes = [IsOwner]
#     lookup_field = "pk"


class CuboidListApiView(generics.ListAPIView):
    model = Cuboid
    queryset = Cuboid.objects.all()
    serializer_class = CuboidSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = CuboidFilter



class CuboidCreateAPIView(generics.CreateAPIView):
	model = Cuboid
	queryset = Cuboid.objects.all()
	serializer_class = CuboidCreateSerializers
	permission_classes = [IsStaff]




class CuboidUpdateAPIView(generics.UpdateAPIView):
	model = Cuboid
	queryset = Cuboid.objects.all()
	serializer_class = CuboidUpdateSerializers
	permission_classes = [IsStaff]
	lookup_field = "pk"
	

class CuboidDeleteAPIView(generics.RetrieveDestroyAPIView):
	model = Cuboid
	queryset = Cuboid.objects.all()
	serializer_class = CuboidSerializer
	permission_classes = [IsOwner]
	lookup_field = "pk"