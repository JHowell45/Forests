import pytest

from woodland.tree_classes import TreeNode


@pytest.fixture()
def child_tree_node() -> TreeNode:
    return TreeNode(
        7,
        {
            1: TreeNode(1),
            3: TreeNode(
                3, {345: TreeNode(345), 654: TreeNode(654), 682: TreeNode(682)}
            ),
            8: TreeNode(8),
            2: TreeNode(2),
        },
    )


@pytest.fixture()
def child_tree_node_two() -> TreeNode:
    return TreeNode(
        9,
        {
            23: TreeNode(23),
            54: TreeNode(54),
            76: TreeNode(76),
            45: TreeNode(45),
        },
    )


@pytest.fixture()
def tree_node_instance(child_tree_node, child_tree_node_two) -> TreeNode:
    return TreeNode(
        5,
        {
            child_tree_node.id: child_tree_node,
            child_tree_node_two.id: child_tree_node_two,
        },
    )
