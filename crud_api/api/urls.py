
from django.urls import path
from .views import(CuboidListApiView, 
	CuboidCreateAPIView, CuboidUpdateAPIView, CuboidDeleteAPIView, APIHomeView)

urlpatterns = [

	path('',APIHomeView.as_view(), name='api_home_page'),
	
    path('api/filter/cuboid_list',CuboidListApiView.as_view(), name='cuboid_list_api'),
    path('api/cuboid_create',CuboidCreateAPIView.as_view(), name='cuboid_create_api'),
    path('api/cuboid_update/<int:pk>',CuboidUpdateAPIView.as_view(), name='cuboid_update_api'),
    path('api/cuboid_delete/<int:pk>',CuboidDeleteAPIView.as_view(), name='cuboid_delete_api'),

]