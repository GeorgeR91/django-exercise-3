from rest_framework import generics, permissions
from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from django.core.paginator import Paginator


class QuoteList(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.IsAdminUser]
