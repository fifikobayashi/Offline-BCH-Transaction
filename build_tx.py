from bitcash import PrivateKeyTestnet
from bitcash.network import NetworkAPI, satoshi_to_currency

# Transaction parameters
privateKey 	 = 'USE_A _TESTNET_PK'
transferCurrency = 'bch'
transferAmount 	 = 0.0001
txDataFile	 = 'offlineTxData.json'
txHexFile	 = 'offlineTxHex.json'
key		 = PrivateKeyTestnet(privateKey)
sendingAddress   = key.address # retrieve instance and address
receivingAddress = 'n2eMqTT929pb1RDNuqEnxdaLau1rxy3efi'

# Build the offline transaction
def prepare_tx():
	print('Wallet address: ' + sendingAddress + '\n>> Balance: ' + satoshi_to_currency(NetworkAPI.get_balance_testnet(sendingAddress), transferCurrency) + ' BCH')
	print('>> Tx value ' + str(transferAmount) + ' ' + transferCurrency)
	tx_data = PrivateKeyTestnet.prepare_transaction(sendingAddress, [(receivingAddress, transferAmount, transferCurrency)])
	output_to_json(txDataFile, tx_data)

# Write the transaction data to a json file	
def output_to_json(jsonFile, tx_data):
	outputStream = open(jsonFile, 'w+')
	outputStream.write(tx_data)
	outputStream.close()
	print('>> Writing to ' + jsonFile + ' was successful')

# Simulate the offline validation and signing of the transaction via JSON string
def sign_tx(txDataFile):
	inputStream = open(txDataFile, 'r')
	transactionData = inputStream.read()
	inputStream.close()
	transactionHex = key.sign_transaction(transactionData)
	print('>> Tx successfully signed \n>> Transaction JSON: ' + transactionHex)
	return transactionHex
	
prepare_tx() # prepares the transaction by building the JSON string with the necessary data
txHex = sign_tx(txDataFile) # simulates the offline signing of the transaction
output_to_json(txHexFile, str(txHex)) # output the tx hex to for subsequent broadcasting (broadcast_tx.py)
