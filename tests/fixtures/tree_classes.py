"""Use this file to define the test fixtures for the tree_classes file.

This file contains and defines the test fixtures for the class and functions
in the 'tree_classes' file.
"""
import pytest
from forests.tree_classes import TreeNode


@pytest.fixture()
def test_tree_node_empty():
    """Use this function to define a test 'TreeNode' instance.

    This function is used for defining a test 'TreeNode' instance to be used
    for testing.

    :return: a 'TreeNode' instance.
    :rtype: TreeNode
    """
    return TreeNode()


@pytest.fixture()
def test_tree_node_base(test_tree_node_payload):
    """Use this fixture to create a base TreeNode instance.

    This fixture is used for creating an instance of the 'TreeNode' class
    with only the payload provided.

    :param test_tree_node_payload: the test payload value.
    :type test_tree_node_payload:
    :return: the test 'TreeNode' instance with only a payload.
    :rtype: TreeNode
    """
    return TreeNode(payload=test_tree_node_payload)


@pytest.fixture()
def test_tree_node_parent(test_tree_node_payload):
    """Use this fixture to create a parent TreeNode instance.

    This fixture is used for creating an instance of the 'TreeNode' class
    with only the payload provided.

    :param test_tree_node_payload: the test payload value.
    :type test_tree_node_payload:
    :return: the test 'TreeNode' instance with only a payload.
    :rtype: TreeNode
    """
    return TreeNode(payload=test_tree_node_payload)


@pytest.fixture()
def test_tree_node_child(test_tree_node_payload):
    """Use this fixture to create a child TreeNode instance.

    This fixture is used for creating an instance of the 'TreeNode' class
    with only the payload provided.

    :param test_tree_node_payload: the test payload value.
    :type test_tree_node_payload:
    :return: the test 'TreeNode' instance with only a payload.
    :rtype: TreeNode
    """
    return TreeNode(payload=test_tree_node_payload)


@pytest.fixture()
def test_tree_node_no_child(test_tree_node_payload,
                            test_tree_node_parent):
    return TreeNode(
        payload=test_tree_node_payload,
        parent=test_tree_node_parent
    )
