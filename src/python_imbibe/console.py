import click
import textwrap

from . import __version__, wiki


@click.command()
@click.version_option(version=__version__)
def main():
    """Python imbibe project"""
    data = wiki.get_wiki_page()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
