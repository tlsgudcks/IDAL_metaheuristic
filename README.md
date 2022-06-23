# IDAL_metaheuristic

(1) findBigNumber.py
  -GA를 이용하여 이진수에 최대값을 찾는 알고리즘 구현
(2) pso.py
  -Particlle swam optimaization을 직접 구현해보고자 만듬
  -일정 바운더리 내에서 랜덤하게 해를 생성하고 0,0이 최적해인 함수에서 잘 수렴하는지를 확인해봄
(3) scheduling_GA-SHIN.py
  -SingleMachineProblem을 GA로 해결해보기 위해 만듬
  -직접 균일분포로 job의 processing time과 due date를 만들고 만들어진 데이터에서 
  total tardiness를 최소화 시키거나 total flowtime을 최소화 시키는 목적함수를 가지고 최적해를 찾음
