"""Console script for docker_registry_cleanup."""
import logging
import sys
import click

from docker_registry_cleanup.docker_registry_cleanup import get_client


@click.group()
def main(args=None):
    pass


@main.command()
@click.option('--namespace', help='The repo to list tags')
@click.option('--repo', help='The repo to list tags')
@click.option('--user', help='The repo to list tags')
@click.option('--pw', help='The repo to list tags')
@click.option('--verbose', help='be verbose')
@click.option('--registry', default='https://hub.docker.com', help='docker registry to connect to')
def list_tags(namespace, repo, user, pw, verbose, registry):
    basic_config_args = {}
    if verbose:
        basic_config_args["level"] = logging.DEBUG

    logging.basicConfig(**basic_config_args)
    client = get_client(registry, user=user, pw=pw)
    repo = client.repository(repository=repo, namespace=namespace)
    print(list(repo.tags())[:10])


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
