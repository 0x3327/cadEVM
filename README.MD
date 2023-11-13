# cadEVM  
![cadEVM](logo.png)


## Table of Contents

- [Project Description & Goals](#project-description--goals)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap & Plans](#roadmap--plans)
- [Contributing](#contributing)


## Project Description & Goals
### Description
cadEVM is a user-friendly Python library designed to streamline the development of radCAD models on the Ethereum Virtual Machine (EVM).

It relies on [Ape framework](https://github.com/ApeWorX/ape) developed by ApeWorx & [radCAD](https://github.com/CADLabs/radCAD) developed by CadLabs, cadEVM prioritizes ease-of-use for token engineers & mechanism designers familiar with cadCAD/radCAD. 

To work effectively with cadEVM, it's essential to be familiar with both the Ape framework and radCAD.

### Goals

1. Simplify the development process for token engineers using EVM.
2. Facilitate mechanism and scenario testing of smart contracts using radCAD and EVM out of the box.
3. Simulate a live environment via forking and ensuring the replication of errors from the network.
4. Create an open-source EVM framework for models that Token Engineers can easily use, especially those familiar with cadCAD/radCAD.


## Installation 

To get started with cadEVM, follow these steps:


1. **Clone the repo**
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install cadEVM:**
   ```bash
   cd cadEVM
   pip install
   ```
## Usage

### Initialization

In the directory of your choice, in the terminal run: `cadEVM init`


You will be prompted to:
1. Enter the name of your project.
2. Indicate whether your contracts are deployed.
3. Specify if you use Alchemy or Infura.
4. Decide whether to install recommended Ape plugins. Afterward, it will install hardhat as the default fork provider in the project directory.


**Deploying a New Project:**

If you haven't deployed contracts yet, initializing the cadEVM project follows the standard Ape framework procedure. The responsibility lies with the token engineer to execute the script for deploying contracts (note that an easy deployer is in development).

**Already Deployed Project:**

For an existing contracts, leverage the Ape Contract instance. You can manually add the ABI or utilize the `ape-etherscan` plugin (included by default) to fetch the ABI from Etherscan. Subsequently, employ the `generate_initial_state` function from the helpers module to create `initial_state_variables` based on the contract's view methods. With `ape-accounts`, you can generate accounts/agents for interactions with the deployed contract.

### Token Template [POC]

To quickly set up a proof of concept, run: `cadEVM token-template` in the directory of your choice. This command downloads the template, showcasing the library's capabilities. All essential plugins will be fetched automatically. The only requirement is obtaining an [Alchemy API key](https://www.alchemy.com/), as the template is configured for Alchemy. If you prefer using Infura, modify the `ape-config.yaml` as follows:



```yaml name: Token template
plugins:
- name: alchemy
- name: hardhat
- name: tokens
- name: etherscan
- name: solidity
- name: vyper
hardhat:
  fork:
    ethereum:
      mainnet:
        upstream_provider: infura #instead of alchemy
        enable_hardhat_deployments: true
```

**Understanding the Template:**

To grasp the underlying logic, the template includes smart contracts and a Python notebook. It serves as a demonstration of this library's usage on both previously developed contracts (like the DAI stablecoin contract) and contracts that are not yet deployed on the network. The template utilizes Hardhat to fork the Ethereum mainnet.

## Roadmap & Plans

1. Develop additional modules to make cadEVM more configurable in terms of both initialization and usage.
2. Create modules to address agent-based properties, enabling the easy creation of different agent types based on assumptions or the current network state.
3. Develop modules to track transaction fees, specific points of interest, etc.
4. Reduce dependence on external frameworks and libraries.
5. Make technical aspects, such as deploying contracts and contract details, more intuitive and user-friendly.

## Contributing

For those eager to contribute:

1. Contribute to this project by forking the repository to your GitHub account.
2. Implement your enhancements or fix issues in your forked repository, ensuring your changes align with the project's goals.
3. Once content with your changes, submit a pull request. Provide details about the modifications made and address relevant issues. Your contributions are highly appreciated!








