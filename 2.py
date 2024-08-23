from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.order import Order
from threading import Thread
import time
from ibapi.contract import Contract
from ibapi.order_state import OrderState

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)

	def openOrder(self, orderId:OrderId , contract:Contract, order:Order, orderState:OrderState):
		print('contract.lastTradeDateOrContractMonth', contract.lastTradeDateOrContractMonth)
		# print('OrderID:', orderId, 'Symbol:', contract.symbol, 'SecType:', contract.secType, 
		# 	'Exchange:', contract.exchange, 'Action:', order.action, 'OrderType:', order.orderType, 
		# 	'TotalQty:', order.totalQuantity, 'Status:', orderState.status, contract.lastTradeDateOrContractMonth)
        
	def orderStatus(self, orderId:OrderId, status:str, filled:float, remaining:float, avgFillPrice:float,
		permId:int, parentId:int, lastFillPrice:float, clientId:int, whyHeld:str, mktCapPrice:float):
		print('OrderID:', orderId, 'Status:', status, 'Filled:', filled, 'Remaining:', remaining, 
			'AvgFillPrice:', avgFillPrice, 'LastFillPrice:', lastFillPrice, 'WhyHeld:', whyHeld)

def run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 7496, 0)

#Start the socket in a thread
api_thread = Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Request list of current open orders
app.reqOpenOrders()

time.sleep(3) #Sleep interval to allow time for incoming order data

app.disconnect()