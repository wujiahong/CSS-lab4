from debug import *
from zoodb import *
import rpclib

def login(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as cc :
        return cc.call('login', username=username, password=password)

def register(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as cc :
        return cc.call('register', username=username, password=password)

def check_token(username, token):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as cc :
        return cc.call('check_token', username=username, token=token)
