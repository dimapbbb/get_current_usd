from datetime import timedelta

from django.utils import timezone
from rest_framework import views
from rest_framework.response import Response

from get_currency.models import CurrencyRequest
from get_currency.services import get_value


class GetCurrencyAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        currency = self.kwargs.get('currency')
        request_data = {
            "currency": currency,
            "value": get_value(char_code=currency)
        }
        last_query_list = CurrencyRequest.objects.filter(currency=currency).order_by('-created_at')[:10]

        if last_query_list:
            if last_query_list[0].created_at + timedelta(seconds=10) > timezone.now():
                return Response({
                        "error": "Между каждым запросом курса должна быть пауза не менее 10 секунд"
                    })

        CurrencyRequest.objects.create(**request_data)
        return Response(
            {
                "currenncy": request_data['currency'],
                "value": request_data['value'],
                "last_query": [str(query) for query in last_query_list] if last_query_list else []
            }
        )
