import pytest

from woodland.tree_classes import Tree


class TestTreeGetterFunctions:
    """Use this class to test the 'Tree' class to test the getters made.

    This function is used for testing the getters for the 'Tree' class. This
    tests to make sure the getters return the correct values and types.
    """

    def test_id_type(self, tree_node_instance):
        """Use this function to test the type of the ID for the 'Tree' instance.

        This function is used for testing the type for the ID value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert isinstance(getattr(tree_node_instance, "id"), int)

    def test_id_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the ID for the 'Tree' instance.

        This function is used for testing the value for the ID value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert getattr(tree_node_instance, "id") == tree_node_instance_data["node_id"]

    def test_payload_type(self, tree_node_instance):
        """Use this function to test the type of the payload for 'Tree'.

        This function is used for testing the type for the payload value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert isinstance(getattr(tree_node_instance, "payload"), (int, float, str))

    def test_payload_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the payload.

        This function is used for testing the value for payload for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert (
            getattr(tree_node_instance, "payload") == tree_node_instance_data["payload"]
        )

    def test_children_type(self, tree_node_instance):
        """Use this function to test the type of the children for 'Tree'.

        This function is used for testing the type for the children value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert isinstance(getattr(tree_node_instance, "children"), dict)

    def test_children_value(self, tree_node_instance):
        """Use this function to test the value of the children for 'Tree'.

        This function is used for testing the value for the children value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert getattr(tree_node_instance, "children") == dict()

    def test_parent_type(self, tree_node_instance):
        """Use this function to test the type of the parent for 'Tree'.

        This function is used for testing the type for the parent value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert (
            isinstance(getattr(tree_node_instance, "parent"), Tree)
            or getattr(tree_node_instance, "parent") is None
        )

    def test_parent_value(self, tree_node_instance, tree_node_instance_data):
        """Use this function to test the value of the parent for 'Tree'.

        This function is used for testing the value for the parent value for the test
        'Tree' instance.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        :param tree_node_instance_data: data used for generating
        :type tree_node_instance_data: dict
        """
        assert (
            getattr(tree_node_instance, "parent") == tree_node_instance_data["parent"]
        )

    def test_repr_type(self, tree_node_instance):
        """Use this function to test the type of the __repr__ function.

        This function is used for testing the type for the 'Tree' test instance
        __repr__ function.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert isinstance(repr(tree_node_instance), str)

    def test_repr_value(self, tree_node_instance):
        """Use this function to test the value of the __repr__ function.

        This function is used for testing the value for the 'Tree' test instance
        __repr__ function.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        assert repr(
            tree_node_instance
        ) == "<Tree ID: {}, Payload: {}, Parent: {}, Child: {}>".format(
            tree_node_instance.id,
            tree_node_instance.payload,
            tree_node_instance.parent,
            tree_node_instance.children,
        )


class TestTreeSetterFunctions:
    """Use this class to test the 'Tree' class to test the setters made.

    This function is used for testing the setters for the 'Tree' class. This
    tests to make sure the setters return the correct values and types.
    """

    test_node_id_options = [10, 2.0]
    test_payload_choices = [1, 1.0]
    test_payload_types = [type(payload) for payload in test_payload_choices]
    test_children_options = [{}, None]
    test_parent_options = [
        None,
        Tree(1, 1, None, None),
        {"node_id": 1, "payload": 1, "children": None, "parent": None},
    ]
    test_parent_expected = [None, Tree(1, 1, None, None), Tree(1, 1, None, None)]

    @pytest.mark.parametrize("node_id", test_node_id_options)
    def test_id_type(self, node_id, tree_node_instance):
        """Use this function to test the type of the ID for the 'Tree' instance.

        This function is used for testing the type for the ID value for the test
        'Tree' instance.

        :param node_id: the test Node ID.
        :type node_id: int/float
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.id = node_id
        assert isinstance(getattr(tree_node_instance, "id"), int)

    @pytest.mark.parametrize("node_id", test_node_id_options)
    def test_id_value(self, node_id, tree_node_instance):
        """Use this function to test the value of the ID for the 'Tree' instance.

        This function is used for testing the value for the ID value for the test
        'Tree' instance.

        :param node_id: the test Node ID.
        :type node_id: int/float
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.id = node_id
        assert getattr(tree_node_instance, "id") == node_id

    @pytest.mark.parametrize(
        "payload,expected", zip(test_payload_choices, test_payload_types)
    )
    def test_payload_type(self, payload, expected, tree_node_instance):
        """Use this function to test the type of the payload for 'Tree'.

        This function is used for testing the type for the payload value for the test
        'Tree' instance.

        :param payload: the test payload to use.
        :type payload: any type.
        :param expected: the type for the payload.
        :type expected: the types for payload.
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.payload = payload
        assert isinstance(getattr(tree_node_instance, "payload"), expected)

    @pytest.mark.parametrize("payload", test_payload_choices)
    def test_payload_value(self, payload, tree_node_instance):
        """Use this function to test the value of the payload.

        This function is used for testing the value for payload for the test
        'Tree' instance.

        :param payload: the test payload to use.
        :type payload: any type.
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.payload = payload
        assert getattr(tree_node_instance, "payload") == payload

    @pytest.mark.parametrize("children", test_children_options)
    def test_children_type(self, children, tree_node_instance):
        """Use this function to test the type of the children for 'Tree'.

        This function is used for testing the type for the children value for the test
        'Tree' instance.

        :param children: the test children to be added.
        :type children: set/dict/None
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.children = children
        assert isinstance(getattr(tree_node_instance, "children"), dict)

    @pytest.mark.parametrize("children", test_children_options)
    def test_children_value(self, children, tree_node_instance):
        """Use this function to test the value of the children for 'Tree'.

        This function is used for testing the value for the children value for the test
        'Tree' instance.

        :param children: the test children to be added.
        :type children: set/dict/None
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.children = children
        assert getattr(tree_node_instance, "children") == dict()

    @pytest.mark.parametrize("parent", test_parent_options)
    def test_parent_type(self, parent, tree_node_instance):
        """Use this function to test the type of the parent for 'Tree'.

        This function is used for testing the type for the parent value for the test
        'Tree' instance.

        :param parent: the test parent to be added to the test Tree instance.
        :type parent: None/Tree/dict
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.parent = parent
        assert (
            isinstance(getattr(tree_node_instance, "parent"), Tree)
            or getattr(tree_node_instance, "parent") is None
        )

    @pytest.mark.parametrize(
        "parent,expected", zip(test_parent_options, test_parent_expected)
    )
    def test_parent_value(self, parent, expected, tree_node_instance):
        """Use this function to test the value of the parent for 'Tree'.

        This function is used for testing the value for the parent value for the test
        'Tree' instance.

        :param parent: the test parent to be added to the test Tree instance.
        :type parent: None/Tree/dict
        :param expected: the expected parent value for the 'Tree' test instance.
        :type expected: None/Tree.
        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.parent = parent
        assert getattr(tree_node_instance, "parent") == expected


class TestTreeMethods:
    """Use this class to test the 'Tree' class to test the methods made.

    This function is used for testing the methods for the 'Tree' class. This
    tests to make sure the methods return the correct values and types.
    """

    test_child = Tree(1, 1, None, None)

    def test_add_child_type(self, tree_node_instance):
        """Use this function to test the 'add_child' function.

        This function is used for testing the type for the 'add_child' function to
        check that a 'Tree' has been successfully added to the list of children.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.add_child(self.test_child)
        assert isinstance(tree_node_instance.children, dict)
        for child_id, child_node in tree_node_instance.children.items():
            assert isinstance(child_id, int)
            assert isinstance(child_node, Tree)

    def test_add_child_value(self, tree_node_instance):
        """Use this function to test the 'add_child' function.

        This function is used for testing the value for the 'add_child' function to
        check that a 'Tree' has been successfully added to the list of children.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        tree_node_instance.add_child(self.test_child)
        assert isinstance(tree_node_instance.children, dict)
        for child_id, child_node in tree_node_instance.children.items():
            assert child_id == self.test_child.id
            assert child_node == self.test_child


class TestTreeErrors:
    """Use this class to test the 'Tree' class to test the errors made.

    This function is used for testing the errors for the 'Tree' class. This
    tests to make sure the errors return the correct values and types.
    """

    def test_set_id_raises_error(self, tree_node_instance):
        """Use this function to check an error is successfully raised.

        This function is used for testing the function raises the correct error code
        when passed an incorrect value.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        with pytest.raises(TypeError):
            tree_node_instance.id = "hello world"

    def test_set_payload_raises_error(self, tree_node_instance):
        """Use this function to check an error is successfully raised.

        This function is used for testing the function raises the correct error code
        when passed an incorrect value.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        with pytest.raises(TypeError):
            tree_node_instance.payload = Tree(1, 1, None, None)

    def test_set_children_raises_error(self, tree_node_instance):
        """Use this function to check an error is successfully raised.

        This function is used for testing the function raises the correct error code
        when passed an incorrect value.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        with pytest.raises(TypeError):
            tree_node_instance.children = Tree(1, 1, None, None)

    def test_set_parent_raises_error(self, tree_node_instance):
        """Use this function to check an error is successfully raised.

        This function is used for testing the function raises the correct error code
        when passed an incorrect value.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        with pytest.raises(TypeError):
            tree_node_instance.parent = "Not a Tree"

    def test_add_child_raise_error(self, tree_node_instance):
        """Use this function to check an error is successfully raised.

        This function is used for testing the function raises the correct error code
        when passed an incorrect value.

        :param tree_node_instance: the test 'Tree' instance.
        :type tree_node_instance: Tree
        """
        with pytest.raises(TypeError):
            tree_node_instance.add_child(1)
