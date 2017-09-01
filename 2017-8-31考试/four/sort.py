#coding=utf-8

#  定义一个排序类，在父类中实现冒泡，插入，选择排序，在子类继承父类下完成快速排序


class ManySort(object):
    def __init__(self,length,l):
        self.length = length
        self.l = l

    def maopao_sort(self):
        for j in range(1,self.length):
            for i in range(0,self.length-j):
                  if self.l[i] > self.l[i+1]:
                      self.l[i],self.l[i + 1] = self.l[i+1],self.l[i]

        print self.l
    
    def select_sort(self):
        for j in range(0,self.length):
            minimum = self.l[j]
            for i in range(j+1,self.length):
                if self.l[i] < minimum:
                    self.l[i],minimum = minimum,self.l[i]
            self.l[j] = minimum
        print self.l

# class ChildSort(ManySort):
#     def __init__(self,length,l):
#         super(ChildSort,self).__init__(length,l) 
#         print self.length



if __name__ == '__main__':
    l = [7,1,5,4,6,2]
    a = ManySort(len(l),l)
    # a.maopao_sort()
    a.select_sort()

    # c = ChildSort()