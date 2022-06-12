from __future__ import annotations

from math import sqrt


class MyQueue:
    def __init__(self) -> None:
        self.first_node = None
        self.last_node = None

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.prev_node = None
            self.next_node = None

    def push(self, data) -> None:
        if self.first_node is None:
            self.first_node = self.Node(data)
            self.last_node = self.first_node
            return

        tmp_node = self.last_node
        self.last_node = self.Node(data)
        tmp_node.next_node = self.last_node
        self.last_node.prev_node = tmp_node

    def pop(self):
        data = self.last_node.data
        if self.first_node == self.last_node:
            self.first_node = None
            self.last_node = None

        else:
            self.last_node = self.last_node.prev_node
            self.last_node.next_node = None

        return data

    def _print(self, node) -> None:
        if node.prev_node:
            self._print(node.prev_node)
        print(node.data, end=", ")

    def print_queue(self) -> None:
        if self.last_node:
            self._print(self.last_node)
            print("")

        else:
            print("queue is empty")

    def size(self) -> int:
        size = 1
        current_node = self.first_node
        while current_node.next_node:
            size += 1
            current_node = current_node.next_node
        return size

    def get_range(self) -> float:
        x1, x2, y1, y2 = self.last_node.data.x, self.first_node.data.x, self.last_node.data.y, self.first_node.data.y
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def search_element(self, x, y) -> int or None:
        current_node = self.first_node
        counter = 0
        while current_node:
            counter += 1
            if current_node.data.x == x and current_node.data.y == y:
                return counter
            current_node = current_node.next_node

        return None

    def delete_queue(self):
        current_node = self.first_node
        size = self.size()

        while size > 0:
            self.pop()
            size -= 1


class Dot:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"
