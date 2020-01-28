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

<img src="/Images/transprob.png"> 

I initialised \[tau\] to 10 for each item initially. The $\mu$ was
defined as: $$\begin{aligned}
    \mu_j = \frac{z_j}{\frac{w_j}{C}}\end{aligned}$$ where $z_j$ is the
value of objected indexed $j$, $w_j$ is the weight of object $j$ and $C$
is the Knapsack capacity. To solve the knapsack problem, I initially
used $\alpha = 3$ and $\beta = 2$ (they are weights of importance we
give to the pheromone trail and the $\mu$), though I note that I am
still arriving at the optimal for fairly a wide range of $\alpha$ and
$\beta$, this is shown in the contour plot below and the optimal
evolution for different values of $\alpha$ and $\beta$. $N_i$ is the set
of available (feasible) objects (we can place inside the knapsack) at a
given stage during the construction of the partial solution. Also, I
used 10 ants for each iteration and 20 iterations for each run of the
ACO. 20 iterations seems enough to converge to the optimal.

The **pheromone update rule** is:

$$\begin{aligned}
    \tau = \tau + \Delta\tau\end{aligned}$$

$\Delta\tau$ is defined as:

$$\Delta\tau = \frac{1}{1 + \frac{z_{\text{best}} - z}{z_{\text{best}}}}$$

During **modelling of evaporation** a key parameter is $\rho$, the rate
of evaporation, which is set at $0.2$, meaning that the pheromone is
reduced by a factor of 0.2 after each iteration with $k$ ants. Also, the
pheromone will never drop below 0.05 so that there is always non-zero
probability of picking a certain item as long as the knapsack capacity
is not violated (see below).

\centering    
\subfigure[Contour plot]{\label{fig:Contour}\includegraphics[width=40mm]{contour.png}}
\subfigure[Average Fitness]{\label{fig:Contour2}\includegraphics[width=70mm]{Alpha_beta_transition.png}}
To check for how often it converges, I ran the Ant Colony Optimization
30 times (for both instances) and it converges every time. Statistics
shown below.

\centering
![Summary for instances
**knapPI\_13\_50\_1000**[]{label="fig:fig5"}](summary.png){#fig:fig5
width="55%"}

\centering
![Summary for instance
**knapPI\_11\_100\_1000.csv**[]{label="fig:fig5"}](summary_oneinstances.png){#fig:fig5
width="55%"}

#### Comparison to Genetic Algorithm: 

Based on the analysis from two instances, the ACO seems much more robust
than the GA. Over $n$ iterations, GA converges lesser number of times
than the ACO which converges every time. Also the run for the ACO takes
lesser time than the GA for each iterations. But a comparison is
difficult based on the fitness calls, since the ACO algorithm does not
directly calculate the fitness while constructing the solution.

#### References:

* \[1\]  "Ant Colony Optimization Algorithm for the 1-0 Knapsack Problem", Krzysztof Schiff, Technical Transactions, 2013.
