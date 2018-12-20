import pytest

from forests.tree_classes import TreeNode


@pytest.fixture(params=[])
def tree_node_instance_data(request):
    return {"id": 0, "payload": request.param, "children": None, "parent": None}


@pytest.fixture()
def tree_node_instance(tree_node_instance_data):
    return TreeNode(**tree_node_instance_data)
