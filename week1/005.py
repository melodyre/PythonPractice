#coding:utf-8
'''
猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，还 不过瘾，
又多吃了一个;第二天早上又将剩下的桃子吃掉一半，又多 吃了一个。
以后每天早上都吃了前一天剩下的一半多一个。到第五天 早上想再吃时，
见只剩下一个桃子了。
请编写程序计算猴子第一天共 摘了多少桃子。

非常简单的一道小学奥数题，每次多吃一个的目的是保证剩下的桃子是偶数，
这样只要从第五天开始反向迭代就能得出原本的桃子数量
'''

tz = 1
for i in range(5):
    tz = (tz + 1) * 2

print tz 
