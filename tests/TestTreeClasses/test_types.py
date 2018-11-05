"""Use this file for testing the return types of the class functions.

This file contains unit tests for testing the functions in the classes in the
tree_classes' file.
"""
import pytest

class TestTreeNode:
	"""Use this class to test the 'TreeNode' class.

	This test class contains test functions for testing the 'TreeNode' class
	to make sure the functions within return the correct type.
	"""

	@pytest.mark.usefixtures('test_tree_node_base')
	def test_empty_tree_node_id(self, test_tree_node_base):
		assert isinstance(getattr(test_tree_node_base, 'node_id'), int)
