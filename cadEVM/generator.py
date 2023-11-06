import os
import click
import yaml

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

    config_data = {}  # An empty dictionary

    with open('ape-config.yaml', 'w') as config_file:
        yaml.dump(config_data, config_file, default_flow_style=False)

if __name__ == "__main__":
    cli()
