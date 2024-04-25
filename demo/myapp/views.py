from django.shortcuts import render, HttpResponse

from rest_framework.response  import Response
from rest_framework.decorators  import api_view
from .models import Catalog
from .serializers import CatalogSerializer
import csv
# Create your views here.

def home(request):
    return HttpResponse('Hello World!')

# get entire catalog from db
@api_view(['GET'])
def getData(request):

    try:
        catalog = Catalog.objects.all()
        ser= CatalogSerializer(catalog, many=True)
        return Response(ser.data)

    except Exception as e:
        return Response({'error': str(e)})

# Update catalog - inserting new rows in database
@api_view(['POST'])
def createCatalog(request):

    # insert data through serializers

    try:
        catArray = request.data
        returnResp = []
        for item in catArray:
            ser = CatalogSerializer(data = item)
            if ser.is_valid():
                ser.save()
                returnResp.append(ser.data)
        return Response(returnResp)
    
    except Exception as e:
        return Response({'error': str(e)})

# Update catalog from uploaded csv file 
@api_view(['POST'])
def csvUpload(request):

    uploaded_file = request.FILES.get('sheet1')
    returnResp = []

    if uploaded_file:
        # Check if the uploaded file is a CSV file
        if not uploaded_file.name.endswith('.csv'):
            return Response({'error': 'Only CSV files are allowed'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the CSV file
        try:
            decoded_file = uploaded_file.read().decode('utf-8')
            reader = csv.DictReader(decoded_file.splitlines())

            # Process each row in the CSV file
            for row in reader:
                ser = CatalogSerializer(data = row)
                
                if ser.is_valid():
                    ser.save()
                    returnResp.append(ser.data)
                

            return Response({'message': 'CSV file uploaded and processed successfully'})
        except Exception as e:
            return Response({'error': str(e)})
    else:
        return Response({'error': 'No file uploaded'})