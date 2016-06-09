#!/usr/bin/python

import rpclib
import sys
import bank
from debug import *

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    def rpc_transfer(self, sender, recipient, zoobars, token):
        return bank.transfer(sender, recipient, zoobars, token)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        return bank.get_log(username)

    def rpc_register(self, username):
        return bank.register(username)
    
(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
