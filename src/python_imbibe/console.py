import click
import textwrap
import requests

from . import __version__

URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """Python imbibe project"""
    with requests.get(URL) as response:
        if response.status_code != 200:
            # response.raise_for_status()
            raise Exception(
                'response code is : {}'.format(response.status_code))
        data = response.json()
        resp_headers = response.headers

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
    click.echo(resp_headers)
