# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 01:02:50 2022

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
assignment=[]
job_endTime={'j1':0, 'j2':0, 'j3':0, 'j4':0} # job의 끝나는 지점을 등록
machine_endTime={'M1':0,'M2':0,'M3':0,'M4':0} # machine의 끝나는 지점을 등록
machine_prejob={'M1':"", 'M2':"",'M3':"", 'M4':""}
job_preOperation={'j1':1,'j2':1,'j3':1,'j4':1}

for i in job_seq:
    lable1 = df.loc[i]          #해당 job과 operation에 해당하는 machine의 p_time을 모아둠
    k=100
    machine_index=0                                 #해당 시퀀스를 기록할 문자
    for j in range(len(lable1)):         #p_time을 돌리면서 가장 적은 p_time을 할당시킴
        if lable1[j]<k:
            k=lable1[j]
            machine_index=j
    assignment.append([i,lable1.index[machine_index]])
print(assignment)
random.shuffle(assignment)
plotlydf = pd.DataFrame([],columns=['Task','Start','Finish','Resource']) #간트차트로 보여주기 위한 데이터프레임
i=0 #간트차트의 인덱싱을 위한 숫자


for jobOp,machine in assignment:  #['j11','M2']의 형태에서 잡과 머신을 가져옴
    job=jobOp[0:2]         #'j11'의 형태를 j1로 
    job_op_seq = int(jobOp[2])
    if job_op_seq != job_preOperation[job]: 
        break
    job_preOperation[job] = job_op_seq+1
    if machine_prejob[machine] == "": #아직 job이 하나도 할당된적 없는 경우
        machine_prejob[machine] = job #현재 머신을 이전에 할당한 job으로 설정함
    df2_sorted = df2[job] #셋업테이블에서 job에 해당하는 컬럼을 가져옴
    setup_time=df2_sorted.loc[machine_prejob[machine]] #컬럼에서 machine에 세팅되어있던 job에서 변경유무 확인
    time = max(machine_endTime[machine] ,job_endTime[job]) #machine과 job의 순서 제약조건을 지키기 위해 더 큰 값을 설정함
    df_sorted = df[machine] #p_time테이블에서 현재 machine에 해당하는 열을 가져옴
    p_time = df_sorted.loc[jobOp] #해당하는 job과 operation의 시간을 가져옴
    start = datetime.fromtimestamp(time*3600) #포매팅 해줌
    time = time+p_time + setup_time # 프로세스타임과 셋업타임을 더해줌
    end = datetime.fromtimestamp(time*3600) #끝나는 시간 포매팅
    plotlydf.loc[i] = dict(Task=job, Start=start, Finish=end, Resource=machine) #간트차트를 위한 딕셔너리 생성, 데이터프레임에 집어넣음
    i += 1 #데이터 프레임 인덱싱 증가
    machine_endTime[machine]=time #기계의 끝나는 시간 설정
    job_endTime[job]=time #job의 끝나는 시간 설정
    print(machine_endTime)
    print(job_endTime)
    machine_prejob[machine] = job #현재 어떤 machine에서 어떤 job을 수행했는지 기록



print(plotlydf)
import plotly.express as px
fig = px.timeline(plotlydf, x_start="Start", x_end="Finish", y="Resource", color="Task", width=1000, height=400)
fig.show()  