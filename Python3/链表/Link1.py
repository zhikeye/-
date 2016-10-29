# -*- coding: utf-8 -*-
"""
链表学习1
"""

class Node:
    """节点"""
    def __init__(self,data,p=0):
        self._data = data
        self._next = p




class Link:
    """链表"""
    def __init__(self):
        self._head = {
            "nodeNum":0,
            "next":0
        }

    def append(self,node):
        """向链表尾部添加一个节点"""
        if int(self._head['nodeNum']) == 0:
            self._head['next'] = node
        else:
            p = self._head['next']
            while p._next != 0:
                p = p._next

            p._next = node

        self._head['nodeNum'] = int(self._head['nodeNum']) + 1
        return True


    def insert(self,node,index=0):
        """向链表指定位置添加节点"""
        if int(self._head['nodeNum']) < index:
            return False
        else:
            if index == 0:
                o = self._head['next']
                node._next = o
                self._head['next'] = node
            else:
                cur = 1
                p = self._head['next']
                while cur < index:
                    p = p._next
                    cur += 1

                o = p._next
                node._next = o
                p._next = node
            self._head['nodeNum'] = int(self._head['nodeNum']) + 1
            return True


    def getLength(self):
        """返回链表的长度"""
        return int(self._head['nodeNum'])

    def getNode(self,index=0):
        """返回指定位置的节点"""
        if int(self._head['nodeNum']) < index:
            return False
        else:
            cur = 0
            p = self._head['next']
            while cur < index:
                p = p._next
                cur += 1

            return p

    def delNode(self,index=0):
        """删除指定位置的节点"""
        if int(self._head['nodeNum']) < index:
            return False
        else:
            if index == 0:
                n = self._head['next']._next
                del self._head['next']
                self._head['next'] = n
                self._head['nodeNum'] = int(self._head['nodeNum']) - 1
            else:
                cur = 1
                p = self._head['next']
                while cur < index:
                    p = p._next
                    cur += 1

                n = p._next._next
                del p._next
                p._next = n
                self._head['nodeNum'] = int(self._head['nodeNum']) - 1

            return True


if __name__ == '__main__':
    node1 = Node("node1")
    node2 = Node("node2")
    node3 = Node("node3")
    node4 = Node("node4")
    node5 = Node("node5")

    link = Link()
    link.append(node1)
    link.append(node2)
    link.insert(node3,1)
    print(link.getLength())
    print('0:',link.getNode(0)._data)
    print('1:',link.getNode(1)._data)
    print('2:',link.getNode(2)._data)
    link.delNode(1)
    print('del 0:',link.getNode(0)._data)
    print('del 1:',link.getNode(1)._data)