from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class MyWrapper(EWrapper):
    def __init__(self):
        self.open_contracts = {}

    def openOrder(self, orderId, contract, order, orderState):
        self.open_contracts[orderId] = contract
        print("Open contract received")

    def error(self, reqId, errorCode, errorString):
        print("Error:", errorCode, errorString)

class MyClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

    def getOpenContracts(self):
        self.reqAllOpenOrders()
wrapper = MyWrapper()
client = MyClient(wrapper)
client.connect('127.0.0.1', 7496, 0)
client.getOpenContracts()


while len(wrapper.open_contracts) == 0:
    pass

# Access the expiration date of open contracts
for order_id, contract in wrapper.open_contracts.items():
    print("Order ID:", order_id)
    print("Contract Symbol:", contract.symbol)
    print("Contract Expiration Date:", contract.lastTradeDateOrContractMonth)