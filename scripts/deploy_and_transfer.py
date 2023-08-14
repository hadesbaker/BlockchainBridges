from scripts.helpful_scripts import get_account
from brownie import accounts, Token, BridgeEth, BridgeStacks
from web3 import Web3

initial_supply = Web3.toWei(50, "ether")


def deploy_and_transfer():
    deployer = get_account()
    recipient = accounts[1]

    token = Token.deploy(initial_supply, {"from": deployer})
    bridge_eth = BridgeEth.deploy(token.address, {"from": deployer})
    bridge_stacks = BridgeStacks.deploy(token.address, {"from": deployer})

    print(token.name())
    print("Token deployed at:", token.address)
    print("BridgeEth deployed at:", bridge_eth.address)
    print("BridgeStacks deployed at:", bridge_stacks.address)

    # Transfer tokens
    token.approve(bridge_eth.address, initial_supply, {"from": deployer})

    # Lock tokens on ETH bridge
    bridge_eth.lockTokens(initial_supply, {"from": deployer})

    # Unlock tokens on STX bridge
    bridge_stacks.unlockTokens(recipient, initial_supply, {"from": deployer})


def main():
    deploy_and_transfer()
