from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from datetime import datetime, timedelta

class MyWrapper(EWrapper):
    def contractDetails(self, reqId, contractDetails):
        contract = contractDetails.contract
        expiration_date = contract.lastTradeDateOrContractMonth

        # Convert expiration date to a datetime object
        expiration_date = datetime.strptime(expiration_date, "%Y%m%d")

        # Calculate the time remaining until expiration
        days_remaining = (expiration_date - datetime.now()).days

        if days_remaining <= 0:
            print("Contract expired!")
        elif days_remaining <= 14:
            print("Contract will expire in 2 weeks!")

    def error(self, reqId, errorCode, errorString):
        print("Error:", errorCode, errorString)

class MyClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

    def getContractDetails(self):
        contract = Contract()
        # Set the contract details as per your requirements
        # For example, you can specify the contract symbol, exchange, etc.
        contract.symbol = "AAPL"
        contract.exchange = "SMART"
        contract.secType = "STK"
        contract.currency = "USD"

        self.reqContractDetails(0, contract)

wrapper = MyWrapper()
client = MyClient(wrapper)
client.connect('127.0.0.1', 7496, 0)

client.getContractDetails()

while len(wrapper.futures_contracts) == 0:
    pass

client.disconnect()