from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Thread
import time

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.open_orders = []

    def openOrder(self, orderId, contract, order, orderState):
        print("OpenOrder. ID:", orderId, contract.symbol, contract.secType, "@", contract.exchange, ":", order.action, order.orderType, order.totalQuantity, orderState.status)
        self.open_orders.append(contract)
        
    def contractDetails(self, reqId, contractDetails):
        print('Contract Expiry:', contractDetails.contract.lastTradeDateOrContractMonth)

def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7496, 0) # Port and clientId might be different in your case

# Start the socket in a thread
api_thread = Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) # Sleep interval to allow time for connection to server

# Request open orders
app.reqOpenOrders()

time.sleep(3) # Sleep interval to allow time for incoming order data

# Request details for each contract associated with the open orders
for contract in app.open_orders:
    app.reqContractDetails(1, contract)

time.sleep(3) # Sleep interval to allow time for incoming data

app.disconnect()