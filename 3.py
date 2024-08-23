from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.order import Order
from threading import Thread
from datetime import datetime, timedelta
import time
from ibapi.contract import Contract
from ibapi.order_state import OrderState

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        # The expiry_dates dictionary could look something like this:
        # { conId1: "2023-06-15", conId2: "2023-07-01", ... }
        # Replace it with your actual data
        self.expiry_dates = {}

    def openOrder(self, orderId:OrderId , contract:Contract, order:Order, orderState:OrderState):
        print('OrderID:', orderId, 'Symbol:', contract.symbol, 'SecType:', contract.secType, 
            'Exchange:', contract.exchange, 'Action:', order.action, 'OrderType:', order.orderType, 
            'TotalQty:', order.totalQuantity, 'Status:', orderState.status)
        
        # Check if the contract is a futures contract

        expiry_date_str = self.expiry_dates.get(contract.conId)
        print('qqqq', expiry_date_str)
        if expiry_date_str:
        # Convert the expiry date to a datetime object
            expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
            print("aaaaaaaaaaa", expiry_date)
        # if contract.secType == "FUT":
        #     # Get the expiry date for this contract
        #     expiry_date_str = self.expiry_dates.get(contract.conId)
        #     if expiry_date_str:
        #         # Convert the expiry date to a datetime object
        #         expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        #         # If the contract is expiring within 14 days, print a message
        #         if expiry_date - datetime.now() <= timedelta(days=14):
        #             print("Hello! Your contract for {} expires in 14 days or less.".format(contract.symbol))
                    
def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7496, 0)

# Start the socket in a thread
api_thread = Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)  # Sleep interval to allow time for connection to server

# Request list of current open orders
app.reqOpenOrders()

time.sleep(3)  # Sleep interval to allow time for incoming order data

app.disconnect()