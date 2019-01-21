"""This file contains the classes for creating Trees.

This file contains the classes for creating Trees along with their functions for
retrieving attributes and generating instances.
"""
from typing import Any, Dict, List, Optional, Union


class Tree:
    """Use this class to create a Node for the tree structure.

    This class is used for creating a 'Tree' Node instance for populating the
    tree data structure with.
    """

    def __init__(
        self,
        node_id: Optional[int] = None,
        payload: Optional[Any] = None,
        children: Optional[Dict[int, "Tree"]] = None,
        parent: Optional["Tree"] = None,
    ) -> None:
        """Use this function to initialise an instance of the Tree class.

        This function is used for initialising an instance of the 'Tree' class
        using the data provided.

        :param node_id: the ID value for the current 'Tree' instance.
        :param payload: the data carried by the 'Tree' instance.
        :param children: a children instance of another 'Tree'.
        :param parent: a parent instance of another 'Tree'.
        """
        self.id = node_id
        self.payload = payload
        self.children = children
        self.parent = parent

    @property
    def id(self) -> int:
        """Use this function to return the ID value for the current instance.

        This function is used for returning the node ID for the current 'Tree'
        instance.

        :return: the ID value for the 'Tree' instance.
        """
        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        """Use this function to set a new ID value for the instance.

        This function is used for setting a new node ID value for the current
        'Tree' instance.

        :param new_id: the new ID value.
        """
        if isinstance(new_id, int):
            self._id = new_id
        elif isinstance(new_id, float):
            print("WARNING: Converting float to integer!")
            self._id = int(new_id)
        else:
            raise TypeError(
                "New ID value for the Tree instance must be of type "
                "int and not: '%s'",
                type(new_id),
            )

    @property
    def payload(self) -> Any:
        """Use this function as a getter for the '_payload' attribute.

        This function is used as a getter function for the '_payload' attribute to
        allow for conditions to be applied to the attribute.

        :return: the value stored in the '_payload' variable.
        """
        return self._payload

    @payload.setter
    def payload(self, new_payload: Any) -> None:
        """Use this function to set a new payload for the current  instance.

        This function is used for updating the payload value for the current
        'Tree' instance.

        :param new_payload: the new payload for the current instance.
        """
        if not isinstance(new_payload, Tree):
            self._payload = new_payload
        else:
            raise TypeError("payload must not be of type Tree!")

    @property
    def children(self) -> List["Tree"]:
        """Use this function as a getter for the '_children' attribute.

        This function is used as a getter function for the '_children' attribute to
        allow for conditions to be applied to the attribute.

        :return: the value stored in the '_children' variable.
        """
        return list(self._children.values())

    @children.setter
    def children(self, new_children: Dict[int, "Tree"]) -> None:
        """Use this function to assign a children to the current instance.

        This function is used for setting a new children 'Tree' to the  current
        'Tree' instance.

        :param new_children: the new children 'Tree' to assign.
        """
        if isinstance(new_children, dict):
            self._children = new_children
        elif new_children is None:
            self._children = dict()
        else:
            raise TypeError("Children passed could not be correctly parsed!")

    @property
    def parent(self) -> "Tree":
        """Use this function as a getter for the '_parent' attribute.

        This function is used as a getter function for the '_parent' attribute to
        allow for conditions to be applied to the attribute.

        :return: the value stored in the '_parent' variable.
        """
        return self._parent

    @parent.setter
    def parent(self, new_parent: Union["Tree", dict]) -> None:
        """Use this function to assign a parent to the current instance.

        This function is used for setting a new parent 'Tree' to the current
        Tree instance.

        :param new_parent: the new parent 'Tree' to assign.
        """
        if isinstance(new_parent, Tree):
            self._parent = new_parent
        elif isinstance(new_parent, dict):
            self._parent = Tree(**new_parent)
        elif new_parent is None:
            self._parent = None
        else:
            raise TypeError(
                "New Parent Must be of type 'Tree', not '{}'!".format(type(new_parent))
            )

    def add_child(self, new_child: "Tree") -> None:
        """Use this function to add another child to the list of children.

        This function is used for appending another child to the list of children for
        the current 'Tree' instance.

        :param new_child: the new 'Tree' to be added to the current instance as a
                          child.
        """
        if isinstance(new_child, Tree):
            self._children[getattr(new_child, "id")] = new_child
        else:
            raise TypeError(
                "Child must be of type 'Tree'! Currently of type: '%s'", type(new_child)
            )

    def __eq__(self, comparison: "Tree") -> bool:
        """Use this function to compare the current instance against another.

        This function is used to override the magic function to correctly compare the
        current 'Tree' instance against another to check they are the same.

        :param comparison: the other 'Tree' instance to compare.
        :return: whether the current instance is equal to the comparison instance.
        """
        return (
            self.id == comparison.id
            and self.payload == comparison.payload
            and self.children == comparison.children
            and self.parent == comparison.parent
        )

    def __repr__(self) -> str:
        """Use this function to create a representation of a 'Tree'.

        This function is used for creating a string representation of a 'Tree'
        instance.

        :return: a string representation of the current instance.
        """
        return "<Tree ID: {}, Payload: {}, Parent: {}, Child: {}>".format(
            self.id, self.payload, self.parent, self.children
        )
