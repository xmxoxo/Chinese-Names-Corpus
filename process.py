#!/usr/bin/env python3
#coding:utf-8

__author__ = 'xmxoxo'

# 读入文件
def readtxtfile(fname):
    pass
    #默认打开模式就为r
    with open(fname,'r',encoding='utf-8') as f:  
        data=f.read()
    return data

#保存文件
def savetofile(txt,filename):
    pass
    with open(filename,'w',encoding='utf-8') as f:  
        f.write(str(txt))
    return 1


#排序
def process (filename):
    txt = readtxtfile(filename)
    lstLine = txt.split('\n')
    lstLine = lstLine[2:]
    lstLine.sort()
    savetofile('\n'.join(lstLine),'./ChengYu_Corpus（5W）-sort.txt')



if __name__ == '__main__':
    pass
    process('./ChengYu_Corpus（5W）.txt')
