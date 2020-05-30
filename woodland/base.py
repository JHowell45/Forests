"""Use this class for defining the base classes for the other TreeNode functions.

This file contains all of the base classes used for creating all of the later tree
structures.
"""


class Node:
    def __init__(
        self,
        value,
        children: "Node" = None,
        parent: "Node" = None,
        max_children: int = None,
    ) -> None:
        self.value = value
        self.children = children or {}
        self.parent = parent
        self.number_of_children = max_children

    def is_root(self) -> bool:
        """Use this function to find out if this node is the root of the tree.

        :return: whether or not this node is the root of the tree.
        """
        return True if self.parent else False

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} Value: {self.value}, Children:"
            f" {self.children}, Parent: {self.parent}, Max Children: "
            f"{self.number_of_children}"
        )
