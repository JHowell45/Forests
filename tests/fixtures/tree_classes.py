import pytest

from woodland.tree_classes import Tree

test_data = [1, 1.0, "hello world"]
test_data_ids = [str(type(data)) for data in test_data]


@pytest.fixture(params=test_data, ids=test_data_ids)
def tree_node_instance_data(request):
    """Use this fixture to create test data for creating the test 'Tree' fixtures.

    This function is used for generating the dictionary used for creating the test
    'Tree' fixtures.

    :param request: allows for several values to be passed as params.
    :return: test Tree data.
    :rtype: dict
    """
    return {"node_id": 0, "payload": request.param, "children": None, "parent": None}


@pytest.fixture()
def tree_node_instance(tree_node_instance_data):
    """Use this function to generate the test 'Tree' instance.

    This function is used for generating the test 'Tree' instance for use for
    testing the attributes and functions.

    :param tree_node_instance_data: the test 'Tree' data.
    :type tree_node_instance_data: dict
    :return: the test 'Tree' instance.
    :rtype: Tree
    """
    return Tree(**tree_node_instance_data)
