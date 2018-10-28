"""This file contains the classes for creating Trees.

This file contains the classes for creating Trees along with their functions
for retrieving attributes and generating instances.
"""


class TreeNode:
    """Use this class to create a Node for the tree structure.

    This class is used for creating a 'TreeNode' Node instance for populating
    the tree data structure with.
    """

    def __init__(self, node_id=None, payload=None, children=None, parent=None):
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
        self.id = node_id
        self._payload = payload
        self._children = [] if children is None else children
        self._parent = parent

    @classmethod
    def from_dict(cls, tree_node_data):
        pass

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
    def payload(self, new_payload):
        """Use this function to set a new payload for the current  instance.

        This function is used for updating the payload value for the current
        'TreeNode' instance.

        :param new_payload: the new payload for the current instance.
        :type new_payload:
        """
        if not isinstance(new_payload, TreeNode):
            self._payload = new_payload
        else:
            raise ValueError('payload must not be of type TreeNode!')

    @property
    def children(self):
        """Use this function as a getter for the '_children' attribute.

        This function is used as a getter function for the '_children' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_children' variable.
        :rtype: TreeNode
        """
        return self._children

    @children.setter
    def children(self, new_children):
        """Use this function to assign a children to the current instance.

        This function is used for setting a new children 'TreeNode' to the
        current TreeNode instance.

        :param new_children: the new children 'TreeNode' to assign.
        :type new_children: TreeNode
        """
        if isinstance(new_children, list):
            self._children = new_children
        else:
            raise ValueError(
                "value must be of type list! Value of type: '%s}'",
                type(new_children)
            )

    def add_child(self, new_child):
        if isinstance(new_child, TreeNode):
            self.children.append(new_child)
        else:
            raise ValueError(
                "Child must be of type 'TreeNode'! Currently of type: '%s'",
                type(new_child)
            )

    @property
    def parent(self):
        """Use this function as a getter for the '_parent' attribute.

        This function is used as a getter function for the '_parent' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_parent' variable.
        :rtype: TreeNode
        """
        return self._parent

    @parent.setter
    def parent(self, new_parent):
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

    def __repr__(self):
        """Use this function to create a representation of a 'TreeNode'.

        This function is used for creating a string representation of a
        'TreeNode' instance.

        :return: a string representation of the current instance.
        :rtype: str
        """
        return (
            '<TreeNode Payload: {}, Parent: {}, Child: {}>'.format(
                    self.payload, self.parent, self.children
            )
        )


class Tree:

    def __init__(self, branches):
        self._branches = branches
