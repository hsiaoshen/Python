#coding=utf-8

# 链表的运算:输入2个列表，通过变成链表的值的相加，若是和大于或等于10，后继数+1，形成一个新的链表

# 链表的初始化和形成

class LinkNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

# 实现链表相加

class LinkAdd(object):
    @staticmethod    
    def to_add(self,L1,L2):
        # 创建新链表的头节点
        H = LinkNode(None)
        p = H
        flag = 0
        while (L1 != None) and (L2 != None):

            # 2个链表的对应位置的值相加小于10
            if(L1.val + L2.val + flag) < 10:
                node = LinkNode(L1.val + L2.val + flag)
                p.next = node
                p = p.next
                flag = 0
            elif (L1.val + L2.val + flag) 

# 将列表转化成链表

def linklist(l):
    H = LinkNode(l[0])
    p = H
    for i in l[1:]:
        node = LinkNode(i)
        p.next = node 
        p = p.next
        
    return H

def main(l1,l2):
    L1 = linklist(l1)
    L2 = linklist(l2)

# 输出列表变成的链表

    # p1 = L1
    # p2 = L2

    # while p1 != None:
    #     print p1.val,'->',
    #     p1 = p1.next
    # print None

    # while p2 != None:
    #     print p2.val,'->',
    #     p2 = p2.next
    # print None

# 进行测试
if __name__ == '__main__':

    l1 = [3,4,5,3]
    l2 = [2,6,4]
    main(l1,l2)