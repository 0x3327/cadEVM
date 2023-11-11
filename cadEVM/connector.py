# TODO make this more configurable with other providers and types of connections
from ape import networks


def connect_mainnet(provider):
    
    provider_mapping = {
        "alchemy": networks.ethereum.mainnet.use_provider("alchemy"),
        "infura": networks.ethereum.mainnet.use_provider("infura"),
    }

    selected_provider = provider_mapping.get(provider)

    if selected_provider is not None:
        return selected_provider.__enter__()
    else:
        raise ValueError("Unsupported provider: {}".format(provider))

def connect_fork():
    return networks.ethereum.mainnet_fork.use_provider("hardhat").__enter__() 

    