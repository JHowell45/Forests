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
def test_tree_node_payload():
    """use this function to define a test payload value for a TreeNode.

    This function is used for defining a test payload value that can be
    passed to a 'TreeNode' instance. This will help for when testing the
    payload value for a

    :return:
    """
    return 'test payload'


@pytest.fixture()
def test_tree_node_no_parent_and_child(test_tree_node_payload):
    return TreeNode(payload=test_tree_node_payload)

@pytest.fixture()
def test_tree_node_no_child(test_tree_node_payload,
                            test_tree_node_no_parent_and_child):
    return TreeNode()
