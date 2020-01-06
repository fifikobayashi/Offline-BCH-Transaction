from bitcash import PrivateKeyTestnet
from bitcash.network import NetworkAPI, satoshi_to_currency

txHexFile = 'offlineTxHex.json'

# parses the tx hex string and broadcasts the tx to the BCH network
def broadcast_tx():
	inputStream = open(txHexFile, 'r')
	transactionHex = inputStream.read()
	inputStream.close()
	broadcastTx = NetworkAPI.broadcast_tx_testnet(transactionHex)
	print(broadcastTx)
	
broadcast_tx()
