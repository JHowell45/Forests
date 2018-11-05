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
	def test_base_tree_node_id(self, test_tree_node_base):
		"""Use this function to test the fixture ID value.

		This function is used for testing the type for the base test
		'TreeNode' instances ID value.

		:param test_tree_node_base: the test base 'TreeNode' instance.
		:type test_tree_node_base: TreeNode
		"""
		assert isinstance(getattr(test_tree_node_base, 'node_id'), int)

	@pytest.mark.usefixtures('test_tree_node_base')
	def test_base_tree_node_payload(self, test_tree_node_base):
		"""Use this function to test the fixture payload value.

		This function is used for testing the type for the base test
		'TreeNode' instances payload value.

		:param test_tree_node_base: the test base 'TreeNode' instance.
		:type test_tree_node_base: TreeNode
		"""
		assert isinstance(
				getattr(test_tree_node_base, 'payload'),
				(int, str, float)
		)
