class TestTreeNodeGetterFunctions:
    def test_id_type(self, tree_node_instance):
        assert isinstance(getattr(tree_node_instance, "id"), int)

    def test_id_value(self, tree_node_instance, tree_node_instance_data):
        assert getattr(tree_node_instance, "id") == tree_node_instance_data["id"]

    def test_payload_type(self, tree_node_instance):
        assert isinstance(getattr(tree_node_instance, "payload"), int)

    def test_payload_value(self, tree_node_instance, tree_node_instance_data):
        assert (
            getattr(tree_node_instance, "payload") == tree_node_instance_data["payload"]
        )

    def test_children_type(self, tree_node_instance):
        assert isinstance(getattr(tree_node_instance, "children"), int)

    def test_children_value(self, tree_node_instance, tree_node_instance_data):
        assert (
            getattr(tree_node_instance, "children")
            == tree_node_instance_data["children"]
        )

    def test_parent_type(self, tree_node_instance):
        assert isinstance(getattr(tree_node_instance, "parent"), int)

    def test_parent_value(self, tree_node_instance, tree_node_instance_data):
        assert (
            getattr(tree_node_instance, "parent") == tree_node_instance_data["parent"]
        )


class TestTreeNodeSetterFunctions:
    pass


class TestTreeNodeClassMethods:
    pass
