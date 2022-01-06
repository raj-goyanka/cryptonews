from django.shortcuts import render
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


# @csrf_protect
@csrf_exempt
def home(request):
    import requests
    import json
    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price=json.loads(price_request.content)    
    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    for d in api['Data']:
        d['body']=d['body'][0:100]+"..."
    return render(request,"home.html",{"api":api,"price":price})



# @csrf_protect
@csrf_exempt
def prices(request):
    if request.method == "POST":
        import requests
        import json
        quote=request.POST.get("quote")
        quote=quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
        crypto=json.loads(crypto_request.content) 
        return render(request,"prices.html",{"quote":quote,"crypto":crypto})
    else:
        notfound="Enter a crypto currency symbol into the above form  ..."
        return render(request,"prices.html",{"notfound":notfound})

