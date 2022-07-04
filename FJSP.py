# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:18:52 2022

@author: parkh
"""
import random
import copy
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('C:/Users/parkh/FJSP.csv',index_col=(0)) #job과 operation을 기록한 테이블
df2 = pd.read_csv('C:/Users/parkh/FJSP_SETUP.csv', index_col=(0)) #setup time 테이블

machine_seq=['M1','M2','M3','M4'] #총 머신 시퀀스
job_seq = ['j11','j12','j13','j14','j15',  #총 job과 operation 시퀀스
            'j21','j22','j23','j24','j25',
            'j31','j32','j33','j34','j35',
            'j41','j42','j43','j44','j45']
assignment={} #할당된 job을 넣어둘 딕셔너리
job_endTime={'j1':0, 'j2':0, 'j3':0, 'j4':0} # job의 끝나는 지점을 등록
machin_endTime={'M1':0,'M2':0,'M3':0,'M4':0} # machine의 끝나는 지점을 등록
machine_prejob={'M1':"", 'M2':"",'M3':"", 'M4':""}
for i in job_seq:
    df_sorted = df[machine_seq]          #machine에 맞게 꺼냄
    lable1 = df_sorted.loc[i]            #해당 job과 operation에 해당하는 machine의 p_time을 모아둠
    k=100                                #가장 긴 프로세스타임
    for j in range(len(lable1)):         #p_time을 돌리면서 가장 적은 p_time을 할당시킴
        if lable1[j]<k:
            k=lable1[j]
            assignment[i] = lable1.index[j]
print(assignment)
assignment = {'j11': 'M2', 'j12': 'M1','j21':  'M2', 'j14': 'M3','j15': 'M1',
              'j42': 'M1', 'j22': 'M3', 'j23': 'M2', 'j24': 'M4','j13': 'M2',
              'j31': 'M4', 'j32': 'M2', 'j33': 'M2', 'j34': 'M2','j35': 'M2',
              'j25': 'M2', 'j41': 'M1', 'j43': 'M2', 'j44': 'M1','j45': 'M2'}

plotlydf = pd.DataFrame([],columns=['Task','Start','Finish','Resource'])
i=0
for key,value in assignment.items():
    key2=key[0:2]
    if machine_prejob[value] == "":
        machine_prejob[value] = key2
    df2_sorted = df2[key2]
    setup_time=df2_sorted.loc[machine_prejob[value]]
    time = max(machin_endTime[value] ,job_endTime[key2])
    df_sorted = df[value]
    p_time = df_sorted.loc[key]
    start = datetime.fromtimestamp(time*3600)
    time = time+p_time + setup_time
    end = datetime.fromtimestamp(time*3600)
    plotlydf.loc[i] = dict(Task=key2, Start=start, Finish=end, Resource=value) #간트차트 보여주기
    i += 1
    machin_endTime[value]=time
    job_endTime[key2]=time
    print(machin_endTime)
    print(job_endTime)
    machine_prejob[value] = key2



print(plotlydf)
import plotly.express as px
fig = px.timeline(plotlydf, x_start="Start", x_end="Finish", y="Resource", color="Task", width=1000, height=400)
fig.show()  