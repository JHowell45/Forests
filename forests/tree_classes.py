"""
"""


class TreeNode:

    def __init__(self, payload, child, parent):
        self._payload = payload
        self._child = child
        self._parent = parent

    @property
    def payload(self):
        return self._payload

    @payload
    def child(self):
        return self._child

    @payload
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
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
