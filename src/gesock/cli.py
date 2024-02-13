import click

from gesock import __version__


@click.command()
def main():
    click.echo(f'whateve mundo ({__version__})')
