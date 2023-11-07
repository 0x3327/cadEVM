import os
import click
import yaml
import subprocess
from collections import OrderedDict

art = """               _ _______     ____  __  
  ___ __ _  __| | ____\ \   / /  \/  | 
 / __/ _` |/ _` |  _|  \ \ / /| |\/| | 
| (_| (_| | (_| | |___  \ V / | |  | | 
 \___\__,_|\__,_|_____|  \_/  |_|  |_| 
 """

@click.group()
def cli():
    pass

@cli.command()
def init():
    print(art)
    project_name = input("Enter the name of your project: ").strip()

    if os.path.exists(project_name):
        print(f"cadEVM project '{project_name}' already exists.")
        return  # Exit the script
    
    existing_contracts = input("Are your contracts already deployed? (y/n): ").strip()

    while True:
        provider = input("Do you choose alchemy or infura as your fork provider? (alchemy/infura): ").strip()
        
        if provider.lower() == 'alchemy':
            p_name = 'alchemy'
            break  # Break out of the loop if the provider is valid
        elif provider.lower() == 'infura':
            p_name = 'infura'
            break  # Break out of the loop if the provider is valid
        else:           
            print("Invalid provider choice. Please choose 'alchemy' or 'infura'.")

    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    if existing_contracts.lower() == 'y':
        folder_names = ['experiments', 'models', 'tests']
        config_data = {
            'name': project_name,
            'plugins': [
        {
            'name': p_name,
        },
        {
            'name': 'hardhat'
        }, 
        {
            'name': 'tokens'
        },
        {
            'name': 'etherscan'
        },
          ],
        'hardhat': {
            'fork': {
                'ethereum': {
                    'mainnet': {
                        'upstream_provider': p_name,
                        'enable_hardhat_deployments': True,
                    },
                },
            },
        }}
     

    elif existing_contracts.lower() == 'n':
        folder_names = ['experiments', 'models', 'tests', 'scripts', 'contracts']
        config_data = {'name': project_name,'plugins': [
        {
            'name': p_name,
        },
        {
            'name': 'hardhat'
        }, 
        {
            'name': 'tokens'
        },
        {
            'name': 'etherscan'
        }, 
        {
            'name': 'solidity'
        },
        {
            'name': 'vyper'
        } ],
        'hardhat': {
            'fork': {
                'ethereum': {
                    'mainnet': {
                        'upstream_provider': p_name,
                        'enable_hardhat_deployments': True,
                    },
                },
            },
        }} 

    
    # Create the folders
    for folder_name in folder_names:
        os.makedirs(folder_name, exist_ok=True)


    with open('ape-config.yaml', 'w') as config_file:
        yaml.dump(config_data, config_file, default_flow_style=False, Dumper=yaml.SafeDumper, sort_keys=False)
    
    install_plugins = input("Do you want to install recommended ape plugins for CadEVM? (y/n): ").strip()
    
    # primitive approach
    if install_plugins.lower() == 'y':
   
        subprocess.run(['ape', 'plugins', 'install', '.'], check=True)

        print("Recommended plugins installed.")

if __name__ == "__main__":
    cli()
