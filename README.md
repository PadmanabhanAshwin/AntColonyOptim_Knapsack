# Solving 1-0 Knapsack Problem using Ant Colony Optimization
### Ashwin Padmanabhan
#### September 2019
---

Ant Colony Optimization for Knapsack problem:
=============================================

This repo deals with the implementation of an Ant-Colony based heuristic to solve the 1-0 Knapsack problem. I have tested this heuristic for the instance name: **knapPI\_13\_50\_1000.csv** and
**knapPI\_11\_100\_1000.csv**.

#### Quick code review: 

The implementation was inspired from the pseudo-code given in
\[1\]. The **transition probability** is given by (probability
that an ant selects a given item to place into the knapsack):

<img src="/Images/transprob.png" align="middle"> 

I initialised \tau to 10 for each item initially. The \mu was
defined as: 

<img src="/Images/mu.png" align="middle"> 
    
where z<sup>-j</sup> is the value of object indexed j, w<sup>-j</sup> is the weight of object j and C
is the Knapsack capacity. To solve the knapsack problem, I initially
used \alpha = 3 and \beta = 2 (they are weights of importance we
give to the pheromone trail and the \mu), though I note that I am
still arriving at the optimal for fairly a wide range of \alpha and
\beta, this is shown in the contour plot below and the optimal
evolution for different values of \alpha and \beta. N<sup>-i</sup> is the set
of available (feasible) objects (we can place inside the knapsack) at a
given stage during the construction of the partial solution. Also, I
used 10 ants for each iteration and 20 iterations for each run of the
ACO. 20 iterations seems enough to converge to the optimal.

The **pheromone update rule** is:
<img src="/Images/tau.png" align="middle" > 
<img src="/Images/deltatau.png" align="middle"> 

During **modelling of evaporation** a key parameter is \rho, the rate
of evaporation, which is set at 0.2, meaning that the pheromone is
reduced by a factor of 0.2 after each iteration with k ants. Also, the
pheromone will never drop below 0.05 so that there is always non-zero
probability of picking a certain item as long as the knapsack capacity
is not violated (see below).

<img src="/Images/contour.png" align="middle" width="250" height="250"> 
<img src="/Images/alpha_beta_transition.png" align="middle" width="250" height="250"> 

To check for how often it converges, I ran the Ant Colony Optimization
30 times (for both instances) and it converges every time. Statistics
shown below.

<img src="/Images/summary.png" align="middle"> 
<img src="/Images/summary_oneinstances.png" align="middle"> 


#### Comparison to Genetic Algorithm: 

Based on the analysis from two instances, the ACO seems much more robust
than the GA. Over n iterations, GA converges lesser number of times
than the ACO which converges every time. Also the run for the ACO takes
lesser time than the GA for each iterations. But a comparison is
difficult based on the fitness calls, since the ACO algorithm does not
directly calculate the fitness while constructing the solution.

#### References:

* \[1\]  "Ant Colony Optimization Algorithm for the 1-0 Knapsack Problem", Krzysztof Schiff, Technical Transactions, 2013.
