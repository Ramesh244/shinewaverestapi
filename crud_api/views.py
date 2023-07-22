from django.shortcuts import render

# Create your views here.
from .models import Employee

from rest_framework import serializers
from .models import Employee
class EmployeeSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
        
class DeleteAllSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

# from crud_api.serializers import EmployeeSerilizers
from rest_framework.viewsets import ModelViewSet
class EmployeeList(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerilizers
    
from rest_framework.response import Response
from rest_framework import status


# class DeleteAllViews(ModelViewSet):
#     queryset=Employee.objects.all()
#     serializer_class=DeleteAllSerializer
    
#     def destroy(self, request, *args, **kwargs):
#         # Get all the records from the queryset
#         all_records = self.get_queryset()
#         # Delete all records
#         all_records.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee


class DeleteAllAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all the records from the queryset
        all_records = Employee.objects.all()
        # Delete all records
        all_records.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetWithName(APIView):
    def get(self, request, *args, **kwargs):
        # Get all the records from the queryset
        all_records = Employee.objects.filter(name__startswith='sa')
        
        # Serialize the queryset using the EmployeeSerializer
        serializer = EmployeeSerilizers(all_records, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data)