# from django.urls import path, include
# from rest_framework.routers import DefaultRouter  # Import DefaultRouter from the correct location

# from .views import EmployeeList,DeleteAllAPIView

# router = DefaultRouter()  # Use DefaultRouter directly from rest_framework.routers
# router.register('emp', EmployeeList),
# from .views import EmployeeList, DeleteAllAPIView

# urlpatterns = [
#     path('', include(router.urls)),  # Use router.urls here to include the URLs from the router
#     path('delete-all/', DeleteAllAPIView.as_view(), name='delete-all-employees'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import the views here, only once
from .views import EmployeeList, DeleteAllAPIView,GetWithName

router = DefaultRouter()
router.register('emp', EmployeeList)

urlpatterns = [
    path('', include(router.urls)),
    path('delete-all/', DeleteAllAPIView.as_view(), name='delete-all-employees'),
   path('getbyname/', GetWithName.as_view(), name='get-all-employees'),

]