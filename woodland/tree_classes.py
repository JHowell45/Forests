"""

"""
from itertools import zip_longest
from typing import Tuple

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    id: int
    children: dict = field(default_factory=dict)

    @classmethod
    def load_from_dict(cls, data: dict) -> "TreeNode":
        node_id = list(data.keys())[0]
        children = tuple(list(data.values())[0].keys())
        node = TreeNode(node_id, {})
        node.add_children_ids(children)
        for id, child in list(data.values())[0].items():
            node.children[id] = TreeNode.load_from_dict({id: child})
        return node

    def add_child(self, child: "TreeNode"):
        self.children[child.id] = child

    def add_child_by_id(self, child_id: int):
        self.children[child_id] = TreeNode(child_id)

    def add_children_ids(self, child_ids: Tuple[int]):
        for child_id in child_ids:
            self.add_child_by_id(child_id)

    def has_children(self) -> bool:
        return bool(self.children)

    def get_next_node(self, id: int) -> "TreeNode":
        return self.children[id]

    def get_node(self, id: int) -> "TreeNode":
        print(f"{self.id}: {list(self.children.keys())} || ID: {id}")
        try:
            return self.get_next_node(id)
        except KeyError:
            for child in self.children.values():
                try:
                    return child.get_node(id)
                except (KeyError, ValueError):
                    pass
        raise ValueError(f"Failed to find the node '{id}'")

    def get_child_path(self, child_id: int) -> Tuple[int]:
        path = [self.id]
        if self.id == child_id:
            return tuple(path)
        try:
            child = self.get_next_node(child_id)
            path.append(child.id)
            return tuple(path)
        except KeyError:
            pass
        for child in self.children.values():
            try:
                path += list(child.get_child_path(child_id))
            except ValueError:
                pass
        if path == [self.id]:
            raise ValueError("Failed to find the specific child in the tree.")
        return tuple(path)

    def get_child_distance(self, child_id: int) -> int:
        return len(self.get_child_path(child_id))

    def distance_between_nodes(self, first_node: int, second_node: int) -> int:
        first_node_path = self.get_child_path(first_node)
        second_node_path = self.get_child_path(second_node)
        print(first_node_path)
        print(second_node_path)
        if first_node_path[0] == second_node_path[0]:
            distance = 0
            for first, second in zip_longest(first_node_path, second_node_path):
                if first == second:
                    pass
                else:
                    if first is None or second is None:
                        distance += 1
                    else:
                        distance += 2
            return distance
        else:
            raise ValueError("Can't calculate the distance")

    def save_as_dict(self) -> dict:
        tree = {self.id: {}}
        for id, child in self.children.items():
            tree[self.id][id] = child.save_as_dict()[id]
        return tree

    def display_tree(self, gap=""):
        print(f"{gap}|-- {self.id}")
        for child in self.children.values():
            new_gap = f"{gap}   "
            child: TreeNode = child
            child.display_tree(gap=new_gap)
