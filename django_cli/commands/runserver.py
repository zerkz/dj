import click
from .run import run


@click.command()
@click.argument('port', required=False)
def runserver(port):
    """Start the Django dev server."""
    args = ['manage.py', 'runserver']
    if port:
        args.append(port)
    run.main(args)
