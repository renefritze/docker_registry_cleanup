"""Main module."""

from docker_registry_client import DockerRegistryClient


def get_client(registry, user, pw):
    # auth_service_url_full = f'{registry}/v2/token'
    cl = DockerRegistryClient(host=registry, api_version=1, username=user, password=pw,
                              )
    # cl._base_client.check_status()
    return cl
