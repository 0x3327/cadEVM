# cadEVM - a library to streamline developing of radCAD models on the EVM. 
![cadEVM](logo.png)


## Table of Contents

- [Project Description & Goals](#Project-Description-&-Goals)
- [Installation](#Installation)
- [Usage](#Usage)
- [Roadmap & Plans](#Roadmap-&-Plans)


## Project Description & Goals
### Descrption
cadEVM is an user-friendly pip library developed in order to streamline developing of radCAD models on the Ethereum Virtual Machine.

It relies heavily on [Ape framework](https://github.com/ApeWorX/ape) developed by ApeWorx & [radCAD](https://github.com/CADLabs/radCAD) developed by CadLabs and focuses on the ease-of-use for the token engineer & mechanism designer familiar with cadCAD/radCAD. 

As the framework uses a lot of Ape framework & radCAD at this stage, familiarity with these frameworks are a requirement. 

As the development continues the library will become more framework independent & customizable, this is just a POC. 

### Goals

1. Enable ease of use for Token Engineers to use EVM
2. Enable mechanism & scenario testing of smart contracts via using radCAD out of the box
3. Create an open source EVM framework for creating Models that Token Engineers can easily use, especially those familiar with cadCAD/radCAD. 


## Installation 

- Clone the repo
- Enter the terminal
- Create a venv in the project directory via `python -m venv venv`    
- activate it via        `source venv/bin/activate`
- run `pip install .` to install cadEVM

## Usage

- In the directory of your choice, in the terminal run `cadEVM init`
- You will be prompted to enter the name of your project, are your contract deployed or not, do you use Alchemy or Infura & do you want to install recommended Ape plugins

- If you do not have a project already deployed the cadEVM project will be initialized like a standard Ape framework project & it is up to the token engineer to run the script to deploy the contracts (easy deployer is going to be developed).Afterwards you can use the `generate_initial_state` from the helpers module to generate the initial_state_variables based on the view methods of the contract. Using `ape-accounts` you can generate accounts/agents that will interact with the deployed contract. Afterwards the project becomes a standard radCAD x Ape project.  

- If you have the project already deployed you can use the ape Contract instance and add the abi manually or `ape-etherscan` plugin to fetch the abi from etherscan. Afterwards you can use the `generate_initial_state` from the helpers module to generate the initial_state_variables based on the view methods of the contract. Using `ape-accounts` you can generate accounts/agents that will interact with the deployed contract. Afterwards the project becomes a standard radCAD x Ape project. 

## Roadmap & Plans

1. Create more modules that will make cadEVM more configurable
2. Create modules that will tackle agent based properties and enable easy creation of agents
3. Create modules that track transaction fees, certain points of interests etc. 
4. Be less dependent on the other frameworks & libraries







