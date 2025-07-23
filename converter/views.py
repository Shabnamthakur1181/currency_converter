from django.shortcuts import render
from django.views import View
import requests

class CurrencyConverterView(View):
    template_name = 'converter/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        amount = float(request.POST.get('amount'))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        converted = round(amount * data["rates"][to_currency], 2)

        return render(request, self.template_name, {
            'result': f"{amount} {from_currency} = {converted} {to_currency}"
        })
