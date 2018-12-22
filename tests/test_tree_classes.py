from forests.tree_classes import TreeNode


class TestTreeNodeGetterFunctions:
    """Use this class to test the 'TreeNode' class to test the getters made.

    This function is used for testing the getters for the 'TreeNode' class. This
    tests to make sure the getters return the correct values and types.
    """

    def test_id_type(self, tree_node_instance):
        """Use this function to test the type of the ID for the 'TreeNode' instance.

        This function is used for testing the type for the ID value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        """
        assert isinstance(getattr(tree_node_instance, "id"), int)

    def test_id_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the ID for the 'TreeNode' instance.

        This function is used for testing the value for the ID value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert getattr(tree_node_instance, "id") == tree_node_instance_data["node_id"]

    def test_payload_type(self, tree_node_instance):
        """Use this function to test the type of the payload for 'TreeNode'.

        This function is used for testing the type for the payload value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        """
        assert isinstance(getattr(tree_node_instance, "payload"), (int, float, str))

    def test_payload_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the payload.

        This function is used for testing the value for payload for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert (
            getattr(tree_node_instance, "payload") == tree_node_instance_data["payload"]
        )

    def test_children_type(self, tree_node_instance):
        """Use this function to test the type of the children for 'TreeNode'.

        This function is used for testing the type for the children value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        """
        assert isinstance(getattr(tree_node_instance, "children"), set)

    def test_children_value(self, tree_node_instance):
        """Use this function to test the value of the children for 'TreeNode'.

        This function is used for testing the value for the children value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        """
        assert getattr(tree_node_instance, "children") == set()

    def test_parent_type(self, tree_node_instance):
        """Use this function to test the type of the parent for 'TreeNode'.

        This function is used for testing the type for the parent value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        """
        assert (
            isinstance(getattr(tree_node_instance, "parent"), TreeNode)
            or getattr(tree_node_instance, "parent") is None
        )

    def test_parent_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the parent for 'TreeNode'.

        This function is used for testing the value for the parent value for the test
        'TreeNode' instance.

        :param tree_node_instance: the test 'TreeNode' instance.
        :type tree_node_instance: TreeNode
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert (
            getattr(tree_node_instance, "parent") == tree_node_instance_data["parent"]
        )


class TestTreeNodeSetterFunctions:
    pass


class TestTreeNodeClassMethods:
    pass


class TestTreeNodeMethods:
    pass
