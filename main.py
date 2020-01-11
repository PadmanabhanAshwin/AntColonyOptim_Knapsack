#%%
import csv
import funcaco as func
import random
import copy
import matplotlib.pyplot as pl
import pandas as pd
#%% Get data
datafilename = "firstinstance.csv"
data = func.importfile(datafilename)

#%% System Parameters

knapsackcapacity = 970 #HARD-CODED
presentknapsackcapacity = knapsackcapacity

#initialprob = func.setinitialprobability(data, knapsackcapacity)
#neighbourhood = func.updateneighbour(neighbourhood, presentknapsackcapacity) Check if data is bad, that is, there exist some element with weight more than knapsack capacity. 

iterations = 20
numants = 10
rho= 0.2

neighbourhood = {i[0]: [int(i[1]), int(i[2]) ] for i in data }
presentneigh = copy.deepcopy(neighbourhood)

tau = {i[0]: 10 for i in data}
mu = {i[0]: ((int(i[1])*presentknapsackcapacity)/int(i[2])) for i in data}
alpha = 3
beta = 2

probmatrix= func.generatetransitionmatrix(presentneigh, tau, mu, alpha, beta)
presentprobmatrix = copy.deepcopy(probmatrix)

a = func.sampleitem(probmatrix)
#%% ACO
func.aco(iterations, neighbourhood, knapsackcapacity, numants, probmatrix, tau, mu, alpha, beta)
#%% Contour plots for different alpha and beta values. 

alpharange = tuple((0.5,10))
betarange = tuple((0.5, 10))
binsize = 3

func.getcountour(alpharange, betarange, binsize, iterations, neighbourhood, knapsackcapacity, numants, probmatrix, tau, mu)
#%% Box Plot and summary
ress= []
for _ in range(30):
    a = func.aco(iterations, neighbourhood, knapsackcapacity, numants, probmatrix, tau, mu, alpha, beta)
    ress.append(a)

#pl.boxplot(ress)
pdress = pd.DataFrame(ress)
summary = pdress.describe()
summary = summary.transpose()
summary.head()
#%%
