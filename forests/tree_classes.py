"""This file contains the classes for creating Trees.

This file contains the classes for creating Trees along with their functions
for retrieving attributes and generating instances.
"""


class TreeNode:
    """Use this class to create a Node for the tree structure.

    This class is used for creating a 'TreeNode' Node instance for populating
    the tree data structure with.
    """

    def __init__(self, payload, child, parent):
        """Use this function to initialise an instance of the TreeNode class.

        This function is used for initialising an instance of the 'TreeNode'
        class.

        :param payload: the data carried by the 'TreeNode' instance.
        :type payload:
        :param child: a child instance of another 'TreeNode'.
        :type child: TreeNode
        :param parent: a parent instance of another 'TreeNode'.
        :type parent: TreeNode
        """
        self._payload = payload
        self._child = child
        self._parent = parent

    @property
    def payload(self):
        """Use this function as a getter for the '_payload' attribute.

        This function is used as a getter function for the '_payload' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_payload' variable.
        :rtype:
        """
        return self._payload

    @payload
    def child(self):
        """Use this function as a getter for the '_child' attribute.

        This function is used as a getter function for the '_child' attribute
        to allow for conditions to be applied to the attribute.

        :return: the value stored in the '_child' variable.
        :rtype: TreeNode
        """
        return self._child

    @payload
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


class Tree:

    def __init__(self, branches):
        self._branches = branches
