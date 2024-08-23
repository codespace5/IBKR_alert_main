from ib_insync import IB, Order

def onOrderStatus(order: Order):
    print(f"Order status: {order}")

# Connect to IBKR
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=0)  # adjust as necessary

# Register for order status updates
ib.orderStatusEvent += onOrderStatus

# Request open orders
open_orders = ib.reqOpenOrders()

for order in open_orders:
    print(f"Open order: {order}")

ib.run()  # Start IB event loop