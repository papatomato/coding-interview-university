# CODING INTERVIEW UNIVERSITY NOTES
## Big O Notation
https://www.youtube.com/watch?v=iOq5kSKqeR4

- O(n) >> the time required to count characters in a string is linear
- len = 1000 (stored number of elements) >> asymptotically constant operation, O(1) >> we already know how many characters
- binary search runs in O(logN) >> array of size 8 runs in 3 operations (log(base2)8), size 16 in log(base2)16 or 4 operations
	+ OMEGA is the best case scenario, in the case of binary search, OMEGA would be if the first middle termwas the term we were looking for
	+ given an array size 3, [1,2,3], if our wanted term is 1 then our program runs in OMEGA(1); if our wanted term is 3, then our program runs in OMEGA(N) (where N represented the length of the array)
- THETA >> best and worst cases are the same

## Quick Tutorial Video
https://www.youtube.com/watch?v=V6mKVRU1evU

- A way to measure how well a computer algorithm scales as the amount of data involved increases.
- 0(1) >> order of one - no matter how the inputs scale, the growth will be the same ***check
- "N" >> the amount of data
- 0(N) >> order of N - the time taken to process grows linearly with the values used
	+ LINEAR SEARCH FOR VALUE
- O(N^2) -> order of N squared - the time taken to process is the size of N squared
	+ BUBBLE SORT
- 0(log n) >> 
	+ BINARY SEARCH
- O(n log n) >> 

...


## Omega and Theta
https://www.youtube.com/watch?v=ei-A_wy5Yxw

- Mathematical Description -
	- f(n) is O(g(n)) if C and n(sub 0)
	f(n) <= Cg(n) for all n>n(sub 0)
	- O(g(n)) vs 'OMEGA'(g(n)) vs 'THETA'

	- 'THETA' => f(n) is 'THETA'(g(n)) if
		1. f(n) is O(g(n))
		2. f(n) is 'OMEGA'(g(n))

- What it all means in the realm of computer science?
	- our time function can show us the dominating term, the part of the equation that requires the most processing power
		+ 4n^2 + 16n + 2 >>> the 4n^2 term will occupy most of the processing as n increases
	- log(base10)(1000) = 3 >>> how many times do you multiply 10 to get 1000? 3
	- log(basex)(n) => O(log(basex)(n)

...


## Asymptotic Notation
https://www.youtube.com/watch?v=gSyDMtdPNpU

- the knapsack problem >> given a problem, a solution may work sometimes and not others and a broken solution may work in different cases
- the RAM Model of Computation
	+ each "simple" operation (+,-,=,if,call) takes 1 step
	+ loops and subroutine calls are not simple operations. they depend on the size of the data and the contents of a subroutine. "Sort" is not a single step operation
	+ each memory acces takes exactly 1 step
	+ we measure the run time of an algorithm by counting the number of steps, where: this model is useful and accurate in the same sense as the flat-earth model (which is useful)
- Worst-Case Complexity >> the function of an algorithm defined by the maximum number of steps taken on any instance of size n >> the most useful case of complexity vs average case and best case
- its easier to talk about upper and lower bounds of the function >> Asumptotic notation or Big O notation (O,Theta,Omega)
- g(n) = O(f(n)) means C x f(n) is an upper bound on g(n)
- g(n) = OMEGA(f(n)) means C x f(n) is a lower bound g(n)
...
- a function multiplied by a constant doesnt change its asymptotics


## Asymptotic Analysis
https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98

- asymptotic analysis - the study of how algorithms behave as the size of the data grows very large or to infinity

### Big Oh Notation is used to represent upper bounds of a function
- let n be the size of programs INPUT
- let T(n) be a function e.g. running time
- let f(n) be another function, preferable simple
- T(n) is in O(f(n)) if and only if T(n) <= Cf(n) >> need a constant, C that will make T(n) less than Cf(n)
- FORMALLY >> O(f(n)) is the set of all functions T(n) that satisfy:
	+ there exist postive constants C and N such that, for all n >= N, T(n) <= cf(n)
	+ N is the place where the vertical line is drawn for the proof
	+ Big O notation doesn't care about (most) constant factors >> unnecessary to write O(2n)
- Big O notation is usually used to indicate dominating (fastest-growing) term
### Table of Important Big O Sets
- smallest to largest >>
----------------------------------------
	FUNCTION   |   COMMON NAME

	O(1)       |   constant
	CO(logn)   |   
	CO
...
- O(nlogn) or faster time: considered "efficient"
- n^7 or slower time: considered useless
- ***need to understand logarithms >> study them if you dont***
- WARNINGS:
	1. fallacious proof >> c must be a constant (can't involve n)
	2. Big O notation does not say what the functions are >> indicates a relationship between the functions	
	3. ...
	4. Big O notation doesn't always tell the whole story

## Amortized Analysis
https://www.youtube.com/watch?v=B3SpQZaAZP4

- opening a duncan donuts >> franchise cost $1,000,000 and cost per donut $1
	+ should the first donut cost $1,000,001? NO. the cost needs to be spread out
	+ assume we will sell 1m donuts, we can sell each donut for $2 each, if we wanted to make a $1 profit we'd need to sell them for $3 a piece
	+ taking a big amount of money and scattering it over time
- Binary Counter - 0000 to 0001 requires 1 unit of working >> 0001 to 0010 is 2 units of work
	+ k = 4 bits >> O(nk)?
	+ every even increment of the binary counter is 1
	+ we always bring some number of people home and send one guy up with a roundtrip ticket (see binary counter example about cost to increment)

## Computational Complexity
https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/

- questions to answer before starting to code: 
	+ is my algorithm worth implementing?
	+ will it solve the largest test cases in time?
	+ if there are other solutions, which should i choose?
- check the number of records and determine if multiple algorithms should be used >> if it is small enough, run algorithm 1, otherwise run algorithm2
- usually we are looking for the behaviour of the program in the worst possible case >> what is the worst input with 700 elements? >> how fast does the maximum runtime grow when we increase the input size?
- an algorithm with runtime proportional to N^2 will always be better than an algorithm with runtime proportional to N^3 on almost all inputs
- f(N) is O(g(N)), if for some c almost the entire graph of the function f is below the graph of the function >> this means that f grows at most as fast as c.g does
- f(N) E O(g(N)) >> we do not use "=" to explain this relationship literally as they are not equal, therefore we can us "E" to denote their relationship
- ^^ defined above is Big O notation and is used to specify upper bounds on function growth
