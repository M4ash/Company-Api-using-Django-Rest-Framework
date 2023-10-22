from rest_framework import serializers
from api.models import Company
from api.models import Employee

#create serializers
#below is also a structure of creating a django form
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    #showing the company id in the api in read only mode
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

#employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    #showing the employee id in the api in read only mode
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"