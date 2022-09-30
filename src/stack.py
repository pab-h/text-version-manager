# https://www.geeksforgeeks.org/abstract-data-types/

from shutil import ExecError
from typing import TypeVar
from typing import List

T = TypeVar("T")

class Stack:
    def __init__(self, max: int | None = None) -> None:
        self.__stack: List[T] = []
        self.__max = max

    @property
    def size(self) -> int:
        return len(self.__stack)
    
    @property
    def max(self) -> int | None:
        return self.__max

    @property
    def isEmpty(self) -> bool:
        return self.size == 0
    
    @property
    def isFull(self) -> bool:
        if self.max == None:
            return False

        return self.max == self.size

    @property
    def stack(self) -> List[T]:
        return self.__stack

    def push(self, item: T) -> None:
        if self.isFull:
            raise Exception("Stack is full")

        self.__stack.append(item)

    def pop(self) -> T:
        if self.isEmpty:
            raise ExecError("Stack is empty")

        return self.__stack.pop()

    def peek(self) -> T:
        return self.__stack[self.size - 1]