from web3 import Web3

infura_url =  "https://mainnet.infura.io/v3/1b9080c337f347a99b40cf72b5c2e26f"

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

# https://etherscan.io/address/0x90e63c3d53e0ea496845b7a03ec7548b70014a91
account = "0x90e63c3d53E0Ea496845b7a03ec7548B70014A91"
balance = web3.eth.getBalance(account)
print(web3.fromWei(balance, "ether"))
