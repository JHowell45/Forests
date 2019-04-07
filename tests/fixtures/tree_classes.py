import pytest

from woodland.tree_classes import TreeNode

test_data = [1, 1.0, "hello world", {"val": 0}]
test_data_ids = [str(type(data)) for data in test_data]


@pytest.fixture(params=test_data, ids=test_data_ids)
def tree_node_instance_data(request):
    """Use this fixture to create test data for creating the test 'TreeNode' fixtures.

    This function is used for generating the dictionary used for creating the test
    'TreeNode' fixtures.

    :param request: allows for several values to be passed as params.
    :return: test TreeNode data.
    :rtype: dict
    """
    return {"node_id": 0, "payload": request.param, "children": None, "parent": None}


@pytest.fixture()
def tree_node_instance(tree_node_instance_data):
    """Use this function to generate the test 'TreeNode' instance.

    This function is used for generating the test 'TreeNode' instance for use for
    testing the attributes and functions.

    :param tree_node_instance_data: the test 'TreeNode' data.
    :type tree_node_instance_data: dict
    :return: the test 'TreeNode' instance.
    :rtype: TreeNode
    """
    return TreeNode(**tree_node_instance_data)
