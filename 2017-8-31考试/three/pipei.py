#coding=utf-8

# 利用正则表达式和re模块完成匹配，含有Django的单词全部存放在一个列表中输出出来

import re

def mate(str):
    pattern = re.compile("\S*Django\S*") 
    k = pattern.findall(str)
    print k




if __name__ == "__main__":
    s = '''
abDjango has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:

Tutorials take you by the hand through a series of steps to create a Web application. Start here if you’re new to Django or Web application development. Also look at the “First steps” below.
Topic guides discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
Reference guides contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.
How-to guides are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Django works.
'''
    mate(s)