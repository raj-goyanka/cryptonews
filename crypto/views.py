from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from requests.auth import HTTPBasicAuth
# from django.views.decorators.csrf import csrf_exempt



@csrf_protect
def home(request):
    import requests
    import json
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36','Accept': 'application/json'}
    auth = HTTPBasicAuth('apikey', '3b534d5731a4ceba131ce5693242ef0c5f6a33b9420c589a83b1c76f31766a70')
    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD",headers=header, auth=auth)
    price=json.loads(price_request.content)    
    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN",headers=header, auth=auth)
    api=json.loads(api_request.content)
    for d in api['Data']:
        d['body']=d['body'][0:100]+"..."
    return render(request,"home.html",{"api":api,"price":price})



@csrf_protect
def prices(request):
    if request.method == "POST":
        import requests
        import json
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36','Accept': 'application/json'}
        auth = HTTPBasicAuth('apikey', '3b534d5731a4ceba131ce5693242ef0c5f6a33b9420c589a83b1c76f31766a')
        quote=request.POST.get("quote")
        quote=quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD",headers=header, auth=auth)
        crypto=json.loads(crypto_request.content) 
        return render(request,"prices.html",{"quote":quote,"crypto":crypto})
    else:
        notfound="Enter a crypto currency symbol into the above form  ..."
        return render(request,"prices.html",{"notfound":notfound})

