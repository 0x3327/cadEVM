import os
import click
import yaml
import subprocess

@click.group()
def cli():
    pass

@cli.command()
def init():
    # Define the folder names you want to create
    folder_names = ['experiments', 'models', 'tests']

    # Create the folders
    for folder_name in folder_names:
        os.makedirs(folder_name, exist_ok=True)
    # TODO fix so ape uses our yaml file as an input for installing plugins
    config_data = {   
      
    'plugins': [
        {
            'name': 'alchemy',
        },
        {
            'name': 'hardhat'
        }
    ]
    }

    with open('ape-config.yaml', 'w') as config_file:
        yaml.dump(config_data, config_file, default_flow_style=False)
    
    # primitive approach
    subprocess.run(['ape', 'plugins', 'install', 'hardhat', 'alchemy'], check=True)

if __name__ == "__main__":
    cli()
