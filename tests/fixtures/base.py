import pytest

from woodland.base import Node


@pytest.fixture()
def base_node_data() -> dict:
    return {}


@pytest.fixture()
def base_node(base_node_data) -> Node:
    return Node(**base_node_data)
