from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your rest framework views here. Company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #Important!!!!! For custom API URL construction, follow this method: 
    #We are gonna make a URL like companies/{primary_Key}/employees to find which employees under which company
    
    #note that its made under company view set so the first url element is companies, 
    # then detail is set to True so we have to put pk id followed by compnaies in the url, 
    # then there is the func name which is employees that will be put at the last url endpoint, 
    # hence the final url should look like this: companies/{primary_Key}/employees

    @action(detail=True, methods=['get']) 
    def employees(self, request, pk=None):
        try:
            mycompany = Company.objects.get(pk=pk) #this is the connection field we are getting
            myemployee = Employee.objects.filter(company = mycompany)
            #now we should serialize
            myemployee_serializer = EmployeeSerializer(myemployee, many = True, context = {'request':request})
            return Response(myemployee_serializer.data) #in json
        
        except Exception as e:
            return Response(
                {
                    'message': 'Company does not exist. Error.'
                }
            )
            


# Create your rest framework views here. Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer