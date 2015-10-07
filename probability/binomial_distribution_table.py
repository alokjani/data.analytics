#!/usr/bin/env python
"""
Author: Alok Jani

binomial_distribution_table.py

Builds Table for calculating probability of 
    r successes in 
    n independent trials, 
    each with probability of success p
"""

import math

def combinatorial(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

def binomial_probability(n,p,x):
    return combinatorial(n,x) * math.pow(p,x) * math.pow(1-p,n - x)


range_n = 20        # Range for number of trials
                    # Range for number of successes is 0 to i for i'th trial
                    # Probability of success is printed at intervals of 0.1 

print
print ' n  r ',
for prob in range(1,10,1):
    p = prob/10.0
    print '%0.4f ' % p,

print 
print "-----------------------------------------------------------------------------"
for n in range(2,range_n+1):
    for x in range(0,n+1):
        print '%2d %2d ' % (n,x),
        for prob in range(1,10,1):
            p = prob/10.0
            px = binomial_probability(n,p,x)
            print '%0.4f ' % (px),
        print
    print 

