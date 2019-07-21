from  django.shortcuts import render
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
import time
def onoff_interface(request):
    return render(request,'x.html',{'msg':''})
def on_off(request):
    pc=PNConfiguration()
    pc.subscribe_key="sub-c-08ab62ec-691c-11e9-912a-e2e853b4b660"
    pc.publish_key="pub-c-4f7ecba5-8d97-45a8-9000-80cb6e5de8ab"
    pc.ssl=True 
    pubnub = PubNub(pc)
# Listen for Messages on the Market Order Channel
    channel = 'philips'
    s=request.GET['btn']
    pubnub.publish().channel(channel).message(s).pn_async(show)
    time.sleep(2)
    return render(request,'x.html',{'msg':''})

def show(msg,stat):
    if(msg and stat):print(msg.timetoken,stat.status_code)
    else:
        print("Error",stat and stat.status_code)
        
