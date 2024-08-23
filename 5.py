from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Thread
import time
from ibapi.client import EClient
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def contractDetails(self, reqId, contractDetails):
        print('Contract expiry: ', contractDetails.contract.lastTradeDateOrContractMonth)

def run_loop():
    app.run()

app = IBapi()
app.connect('127.0.0.1', 7496, 0) # Port and clientId might be different in your case

# Start the socket in a thread
api_thread = Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) # Sleep interval to allow time for connection to server

# Define the contract
contract = Contract()
contract.symbol = 'AAPL' # This should be replaced by your contract symbol
contract.secType = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'
contract.lastTradeDateOrContractMonth = '202209' # This should be replaced by your contract's last trading date or month

# Request contract details
app.reqContractDetails(1, contract)

time.sleep(3) # Sleep interval to allow time for incoming data

app.disconnect()