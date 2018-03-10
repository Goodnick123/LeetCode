# -*- coding: utf-8 -*-
# @Time    : 18-3-6 下午4:19
# @Author  : Yeh
# @File    : GA_BLEG.py
# @Software: PyCharm

import math
import random

class GA_BLEG():
    def __init__(self,xlength,xcount,ylength,ycount):
        # x染色体长度
        self.xlength = xlength
        # x种群中的染色体数量
        self.xcount = xcount
        # 随机生成初始x种群
        self.xpopulation = self.gen_population(xlength, xcount)
        # y染色体长度
        self.ylength = ylength
        # y种群中的染色体数量
        self.ycount = ycount
        # 随机生成初始y种群
        self.ypopulation = self.gen_population(ylength, ycount)

    def evolve(self,retain_rate=0.2,random_select_rate=0.5, mutation_rate=0.01):
        """
        进化
        对当前一代种群依次进行选择、交叉并生成新一代种群，然后对新一代种群进行变异
        """
        xparents,yparents =self.selection(retain_rate,random_select_rate)
        self.crossover(xparents,yparents)

        self.mutation(mutation_rate,self.xpopulation,self.xlength)
        self.mutation(mutation_rate,self.ypopulation,self.ylength)

    def result(self,xpopulation,xlength,ypopulation,ylength):
        """
        获得当前代的最优值，这里取的是函数取最大值时x的值。
        """
        graded = [(self.fitness(xchromosome, xlength, ychromosome, ylength), (xchromosome, ychromosome)) for
                  xchromosome, ychromosome in zip(xpopulation, ypopulation)]
        graded = [x[1] for x in sorted(graded)]
        print(graded[0])
        return self.decode(graded[0][0],xlength),self.decode(graded[0][1],ylength)


    def selection(self,retain_rate, random_select_rate):
        """
        选择先对适应度从大到小排序，选出存活的染色体
        再进行随机选择，选出适应度虽然小，但是幸存下来的个体
        """
        # 对适应度从大到小进行排序
        graded = [(self.fitness(xchromosome,self.xlength,ychromosome,self.ylength), (xchromosome,ychromosome)) for xchromosome,ychromosome in zip(self.xpopulation,self.ypopulation)]
        #print(sorted(graded))
        graded = [x[1] for x in sorted(graded) ]

        # 选出适应性强的染色体
        retain_length = int(len(graded) * retain_rate)
        parents = graded[:retain_length]
        xparents=[]
        yparents=[]
        for x,y in parents:
            xparents.append(x)
            yparents.append(y)
        # 选出适应性不强，但是幸存的染色体
        for xchromosome ,ychromosome in graded[retain_length:]:
            if random.random() < random_select_rate:
                xparents.append(xchromosome)
                yparents.append(ychromosome)
        return xparents,yparents

    def mutation(self, rate,population,length):
        """
        变异
        对种群中的所有个体，随机改变某个个体中的某个基因
        """
        for i in range(len(population)):
            if random.random() < rate:
                j = random.randint(0, length-1)
                population[i] ^= 1 << j

    def crossover(self,xparents,yparents):
        """
        染色体的交叉、繁殖，生成新一代的种群
        """
        # 新出生的孩子，最终会被加入存活下来的父母之中，形成新一代的种群。
        xchildren = []
        ychildren = []
        # 需要繁殖的孩子的量
        target_count = len(self.xpopulation) - len(xparents)
        # 开始根据需要的量进行繁殖
        while len(xchildren) < target_count:
            male = random.randint(0, len(xparents)-1)
            female = random.randint(0, len(xparents)-1)
            if male != female:
                # 随机选取交叉点
                cross_pos = random.randint(0, self.xlength)
                # 生成掩码，方便位操作
                mask = 0
                for i in range(cross_pos):
                    mask |= (1 << i)
                xmale = xparents[male]
                xfemale = xparents[female]
                ymale =yparents[male]
                yfemale =yparents[female]
                # 孩子将获得父亲在交叉点前的基因和母亲在交叉点后（包括交叉点）的基因
                xchild = ((xmale & mask) | (xfemale & ~mask)) & ((1 << self.xlength) - 1)
                xchildren.append(xchild)
                ychild = ((ymale & mask) | (yfemale & ~mask)) & ((1 << self.ylength) - 1)
                ychildren.append(ychild)
        # 经过繁殖后，孩子和父母的数量与原始种群数量相等，在这里可以更新种群。
        self.xpopulation = xparents + xchildren
        self.ypopulation = yparents + ychildren

    def fitness(self, xchromosome,xlength,ychromosome,ylength):
        """
        计算适应度，将染色体解码为0~9之间数字，代入函数计算
        因为是求最大值，所以数值越大，适应度越高
        """
        x = self.decode(xchromosome,xlength)
        y = self.decode(ychromosome,ylength)

        return abs(20-4*x-2*y)+abs(8-x-y)+abs(12-3*x-y)


    def gen_population(self, length, count):
        """
        获取初始种群（一个含有count个长度为length的染色体的列表）
        """
        return [self.gen_chromosome(length) for i in range(count)]

    def decode(self, chromosome,length):
        """
        解码染色体，将二进制转化为属于[0, 9]的实数
        """
        return chromosome * 9.0 / (2 ** length - 1)

    def gen_chromosome(self, length):
        """
        随机生成长度为length的染色体，每个基因的取值是0或1
        这里用一个bit表示一个基因
        """
        chromosome = 0
        for i in range(length):
            chromosome = chromosome | ((1 << i) * random.randint(0, 1))
        return chromosome

if __name__ == '__main__':
    # 染色体长度为17， 种群数量为300
    ga = GA_BLEG(17,300,17,300)

    # 200次进化迭代
    for x in range(1000):
         ga.evolve()

    print(ga.result(ga.xpopulation,ga.xlength,ga.ypopulation,ga.ylength))

