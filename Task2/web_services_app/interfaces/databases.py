from abc import ABC, abstractclassmethod


class Database(ABC):

    @abstractclassmethod
    def conn():
        raise Exception("Need implement the´method: ´connection´")

    @abstractclassmethod
    def insert():
        raise Exception("Need implement the method: ´insert´")

    @abstractclassmethod
    def select():
        raise Exception("Need implement the method: ´select´")

    @abstractclassmethod
    def delete():
        raise Exception("Need implement the method: ´delete´")
