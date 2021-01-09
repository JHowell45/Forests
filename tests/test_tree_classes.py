import pytest


class TestTreeNode:
    def test_root_id(self, tree_node_instance):
        assert tree_node_instance.id == 5

    def test_get_next_node_first(self, tree_node_instance, child_tree_node):
        assert tree_node_instance.get_next_node(child_tree_node.id) == child_tree_node

    def test_get_next_node_second(self, tree_node_instance, child_tree_node_two):
        assert (
            tree_node_instance.get_next_node(child_tree_node_two.id)
            == child_tree_node_two
        )
