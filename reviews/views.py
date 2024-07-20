from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.db import transaction
import pandas as pd
import io
from rest_framework import viewsets, status

from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FileUploadView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_data = request.FILES.get('file')
        if not file_data:
            return Response({
                "message": "No file provided",
                "status": 400
            }, status=status.HTTP_400_BAD_REQUEST)

        if not self.is_valid_csv(file_data):
            return Response({
                'message': 'Input file should be CSV',
                'status': 422
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        df = pd.read_csv(io.StringIO(file_data.read().decode('utf-8')))
        
        # Perform data cleaning
        df = df.drop(columns=['other info', 'review id', 'group id', 'sentiment date', 'customer name'])
        df['aspect sentiment'] = pd.to_numeric(df['aspect sentiment'], errors='coerce')
        df['overall sentiment'] = pd.to_numeric(df['overall sentiment'], errors='coerce')
        df['stars count'] = df['stars count'].str.extract(r'(\d\.\d)').astype(float)
        df = df.dropna()

        with transaction.atomic():
            for _, row in df.iterrows():
                review = Review(
                    retailer=row['retailer'],
                    region=row['region'],
                    category=row['category'],
                    product_name=row['product name'],
                    brand=row['brand'],
                    review=row['review'],
                    aspect=row['aspect'],
                    aspect_sentiment=row['aspect sentiment'],
                    overall_sentiment=row['overall sentiment'],
                    scrape_date=row['scrape date'],
                    stars_count=row['stars count']
                )
                review.save()

        return Response({
            "message": "File processed successfully",
            "status": 201
        }, status=status.HTTP_201_CREATED)

    def is_valid_csv(self, file_data):
        return file_data.name.split('.')[-1] == 'csv'
