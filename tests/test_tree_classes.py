class TestTreeNodeGetterFunctions:
    def test_id_type(self, tree_node_instance):
        assert isinstance(getattr(tree_node_instance, "id"), int)

    def test_id_value(self, tree_node_instance, tree_node_instance_data):
        assert getattr(tree_node_instance, "id") == tree_node_instance_data["id"]


class TestTreeNodeSetterFunctions:
    pass


class TestTreeNodeClassMethods:
    pass
