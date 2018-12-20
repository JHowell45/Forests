"""This file contains the classes for creating Trees.

This file contains the classes for creating Trees along with their functions
for retrieving attributes and generating instances.
"""


class TreeNode:
    """Use this class to create a Node for the tree structure.

    This class is used for creating a 'TreeNode' Node instance for populating
    the tree data structure with.
    """

    def __init__(
        self,
        node_id: int = None,
        payload=None,
        children: set = None,
        parent: "TreeNode" = None,
    ) -> None:
        """Use this function to initialise an instance of the TreeNode class.

        This function is used for initialising an instance of the 'TreeNode'
        class.

        :param node_id: the ID value for the current 'TreeNode' instance.
        :type node_id: int
        :param payload: the data carried by the 'TreeNode' instance.
        :type payload:
        :param children: a children instance of another 'TreeNode'.
        :type children: TreeNode
        :param parent: a parent instance of another 'TreeNode'.
        :type parent: TreeNode
        """
        self.node_id = node_id
        self.payload = payload
        self.children = children
        self.parent = parent

    @classmethod
    def from_dict(cls, tree_node_data: dict) -> "TreeNode":
        """Use this function to create a 'TreeNode' instance using a dict.

        This function is used for creating a 'TreeNode' instance using a
        python dictionary.

        :param tree_node_data: the 'TreeNode' data dictionary.
        :type tree_node_data: dict
        :return: a generated instance of a 'TreeNode'.
        :rtype: dict
        """
        parent_node: TreeNode = TreeNode.from_dict(tree_node_data["parent"])
        children: set = {
            TreeNode.from_dict(child) for child in tree_node_data["children"]
        }
        return cls(
            node_id=tree_node_data["id"],
            payload=tree_node_data["payload"],
            children=children,
            parent=parent_node,
        )

    @property
    def node_id(self) -> int:
        """Use this function to return the ID value for the current instance.

        This function is used for returning the ID for the current
        'TreeNode' instance.

        :return: the ID value for the 'TreeNode' instance.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, new_id: int) -> None:
        """Use this function to set a new ID value for the instance.

        This function is used for setting a new ID value for the current
        'TreeNode' instance.

        :param new_id: the new ID value.
        :type new_id: int
        """
        if isinstance(new_id, int):
            self._node_id = new_id
        elif isinstance(new_id, float):
            print("WARNING: Converting float to integer!")
            self._node_id = int(new_id)
        else:
            raise TypeError(
                "New ID value for the TreeNode instance must be of type "
                "int and not: '%s'",
                type(new_id),
            )

    @property
    def payload(self):
        """Use this function as a getter for the '_payload' attribute.

        This function is used as a getter function for the '_payload' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_payload' variable.
        :rtype:
        """
        return self._payload

    @payload.setter
    def payload(self, new_payload) -> None:
        """Use this function to set a new payload for the current  instance.

        This function is used for updating the payload value for the current
        'TreeNode' instance.

        :param new_payload: the new payload for the current instance.
        :type new_payload:
        """
        if isinstance(new_payload, TreeNode):
            self._payload = new_payload
        else:
            raise ValueError("payload must not be of type TreeNode!")

    @property
    def children(self) -> set:
        """Use this function as a getter for the '_children' attribute.

        This function is used as a getter function for the '_children' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_children' variable.
        :rtype: TreeNode
        """
        return self._children

    @children.setter
    def children(self, new_children: set) -> None:
        """Use this function to assign a children to the current instance.

        This function is used for setting a new children 'TreeNode' to the
        current TreeNode instance.

        :param new_children: the new children 'TreeNode' to assign.
        :type new_children: TreeNode
        """
        if isinstance(new_children, list):
            self._children = new_children
        elif new_children is None:
            self._children = set()
        else:
            raise ValueError(
                "value must be of type list! Value of type: '%s}'", type(new_children)
            )

    def add_child(self, new_child: "TreeNode") -> None:
        """Use this function to add another child to the list of children.

        This function is used for appending another child to the list of
        children for the current 'TreeNode' instance.

        :param new_child: the new 'TreeNode' to be added to the current
                          instance as a child.
        :type new_child: TreeNode
        """
        if isinstance(new_child, TreeNode):
            self._children.add(new_child)
        else:
            raise ValueError(
                "Child must be of type 'TreeNode'! Currently of type: '%s'",
                type(new_child),
            )

    @property
    def parent(self) -> "TreeNode":
        """Use this function as a getter for the '_parent' attribute.

        This function is used as a getter function for the '_parent' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_parent' variable.
        :rtype: TreeNode
        """
        return self._parent

    @parent.setter
    def parent(self, new_parent: "TreeNode") -> None:
        """Use this function to assign a parent to the current instance.

        This function is used for setting a new parent 'TreeNode' to the
        current TreeNode instance.

        :param new_parent: the new parent 'TreeNode' to assign.
        :type new_parent: TreeNode
        """
        if isinstance(new_parent, TreeNode):
            self._parent = new_parent
        else:
            raise TypeError(
                "New Parent Must be of type 'TreeNode', not '{}'!".format(
                    type(new_parent)
                )
            )

    def __repr__(self) -> str:
        """Use this function to create a representation of a 'TreeNode'.

        This function is used for creating a string representation of a
        'TreeNode' instance.

        :return: a string representation of the current instance.
        :rtype: str
        """
        return "<TreeNode ID: {}, Payload: {}, Parent: {}, Child: {}>".format(
            self.node_id, self.payload, self.parent, self.children
        )


class Tree:
    def __init__(self, branches):
        self._branches = branches
