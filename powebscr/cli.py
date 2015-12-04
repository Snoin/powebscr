from click import group


@group()
def cli():
    """Command line interface for powwebscr."""

main = cli
