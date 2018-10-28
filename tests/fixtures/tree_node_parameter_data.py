"""Use this file to declare the parameter fixture functions.

This file contains the fixtures defining the parameters for a test 'TreeNode'
fixture instance.
"""
import pytest

payload_data = [
	'test payload',
	10,
	23.54,
	True
]

payload_ids = [
	'string',
	'integer',
	'float',
	'boolean'
]


@pytest.fixture(params=payload_data, ids=payload_ids)
def test_tree_node_payload(request):
	"""use this fixture to define a test payload value for a TreeNode.

	This fixture is used for defining a test payload value that can be
	passed to a 'TreeNode' instance. This will help for when testing the
	payload value for a

	:return: a test payload value.
	:rtype:
	"""
	return request.param


@pytest.fixture()
def test_tree_node_id():
	"""Use this fixture to create an ID value for the test 'TreeNode' instance.

	This function is used for defining a test ID value for the test
	'TreeNode' instances.

	:return: test ID value.
	:rtype: int
	"""
	return 0
