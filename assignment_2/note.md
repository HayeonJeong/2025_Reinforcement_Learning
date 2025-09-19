# State Value Function $V(s)$ (Q2.1)

- 정책(랜덤 정책) 주어져 있음  
- 구해야 하는 건 모든 상태에서의 기대 return임  
- Bellman 기대 방정식은 자기 자신을 포함하는 재귀식임  

$$V(s) = \sum_a \pi(a|s)\sum_{s'} P(s'|s,a)\big(R(s,a,s') + \gamma V(s')\big)$$

- 위 식을 바로 풀 수 없음  
- 따라서 **반복(iteration)**을 통해 점점 근사해서 수렴시켜야 함  
- 이게 Iterative Policy Evaluation 또는 **Value Iteration (prediction 버전)**임  

---

# Action Value Function $Q(s,a)$ (Q2.2)

- $Q(s,a)$는 정의상 즉각적 보상 + 다음 상태의 가치로 표현됨  

$$Q(s,a) = \sum_{s'} P(s'|s,a)\big(R(s,a,s') + \gamma V(s')\big)$$

- 이미 수렴된 $V(s)$가 있으면, 한 번 계산으로 바로 나옴  
- 더 이상 반복 필요 없음  
