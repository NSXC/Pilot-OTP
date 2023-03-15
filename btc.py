from bitcoinlib.wallets import wallet_delete
from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service
from bitcoinlib.mnemonic import Mnemonic
import string
import random
import time
#Working out BTC addresses

N = 40
res = ''.join(random.choices(string.ascii_letters, k=N))
mnemonic = Mnemonic().generate()
w = Wallet.create(str(res), network='bitcoin')
temp_address = w.get_key().address
print("Temporary Bitcoin Address:", temp_address)

required_amount = 0.001 
main_wallet_address = '' 

service = Service()
try:
    for i in range(30):
        utxos = service.getutxos(temp_address)
        total_received = sum([utxo['value'] for utxo in utxos]) / 10**8 
        if total_received >= required_amount:
            print(f"Received {total_received} BTC. Initiating transfer to main wallet.")
            service.send_to_address(main_wallet_address, total_received, from_address=temp_address)
            print("Transfer completed.")
            break
        else:
            print(f"Waiting for {required_amount - total_received} BTC to be received...")

        if i == 5:
            wallet_delete(w.name)
            print("Wallet deleted from the database.")
        else:
            time.sleep(10) 
except Exception as e:
    print("Error:", e)
finally:
    wallet_delete(w.name)
    print("Wallet deleted from the database.")