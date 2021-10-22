'''
To run, python -i find_counterexamples.py MAX_K

MAX_K should be an integer, which is the largest k that will be checked. This is
so the program knows how many primes to precompute before doing anything.

'''


import math
import sys

min_k = 16
max_k = int(sys.argv[1])


# Precomputing all the primes we're going to need:
primes = [True]*int(math.floor(math.sqrt(2*max_k))+20)
p = 2
while p < len(primes)/2:
    i=2
    while i*p < len(primes):
        primes[i*p] = False
        i+=1
    p+=1
    while not primes[p]:
        p+=1
primes[0] = False
primes[1] = False

primes = [i for i in range(len(primes)) if primes[i]]
# primes should now be a list of every prime less than sqrt(max_k), and a few more above that.


# This is to set whether to count prime multiples as multiples, and whether or not to use
#   and adjusted version of Proposition A/B/C that would account for this
def set_functions(M, R):
    global mins_function, run_function
    if M:
        mins_function = min_remainings_changed_props
    else:
        mins_function = min_remainings
    if R:
        run_function = run_discount_primes
    else:
        run_function = run


# This generates the index of P for a given k. I.e primes[get_P_i(k)] is the largest
#   prime less than or equal to the squareroot of 2k.
def get_P_i(k):
    s = math.sqrt(2*k)
    P_i=-1
    for i in range(len(primes)):
        if primes[i]<=s and primes[i+1]>s:
            P_i = i
            break
    if P_i==-1:
        assert False
    return P_i


# This runs the process of removing pairs containing multiples of primes, starting
#   with P and going down P_1, P_2, ... , 2.
# This function returns a list of numbers of pairs remaining after each P_i.
def run(k):
    pairs = [(i, 2*k-i) for i in range(1,k)]
    P_i = get_P_i(k)
    removed_pairs = []
    numbersof_pairs_removed = []
    i = P_i
    while i >= 0:
        P = primes[i]
        n_remov = 0
        for pair_index in range(len(pairs)):
            pair = pairs[pair_index]
            if (pair[0]%P) * (pair[1]%P) == 0:
                if pair_index not in removed_pairs:
                    removed_pairs += [pair_index]
                    n_remov += 1
        numbersof_pairs_removed += [n_remov]
        i+=-1
    remaining_each_round = [k]
    for rm in numbersof_pairs_removed:
        remaining_each_round += [remaining_each_round[-1] - rm]
    return remaining_each_round


def run_discount_primes(k, verbose=False):
    pairs = [(i, 2*k-i) for i in range(1,k)]
    P_i = get_P_i(k)
    removed_pairs = []
    numbersof_pairs_removed = []
    i = P_i
    while i >= 0:
        P = primes[i]
        n_remov = 0
        for pair_index in range(len(pairs)):
            pair = pairs[pair_index]
            if (pair[0]%P==0 and pair[0]!=P) or (pair[1]%P==0 and pair[1]!=P):
                if pair_index not in removed_pairs:
                    removed_pairs += [pair_index]
                    n_remov += 1
        numbersof_pairs_removed += [n_remov]
        if verbose:
            print(f"Removed after P={P}:\n{sorted([ min(pairs[j]) for j in removed_pairs ])}")
        i+=-1
    remaining_each_round = [k]
    for rm in numbersof_pairs_removed:
        remaining_each_round += [remaining_each_round[-1] - rm]
    return remaining_each_round


# This function computes the supposed lower bound according to Proposition B and C
#   for the values returned by run(k).
def min_remainings(k):
    P_i = get_P_i(k)
    mr = [k]
    i = P_i
    while i >= 0:
        P = primes[i]
        mr += [mr[-1] * (1-2/P)]
        i+=-1
    return mr



# This function computes the supposed lower bound according to
#   a changed version of Proposition A, B and C, where the first
#   multiple of each prime is not counted, since it is itself prime.
def min_remainings_changed_props(k):
    P_i = get_P_i(k)
    mr = [k]
    i = P_i
    while i >= 0:
        P = primes[i]
        mr += [mr[-1] * (1+(1/k)-(2/P))]
        i+=-1
    return mr



# This compares outputs of run(k) and min_remainings(k) for many values of k.
# mk is that maximum value of k to be tried.
# tolerance can be set to only print out erroneous examples where the error is
#   greater than tolerance.
def try_many(mk, tolerance=0):
    mk = min(mk, max_k)
    for k in range(min_k, mk):
        actual = run_function(k)
        mins = mins_function(k)
        if not all([ actual[i] >= mins[i]-tolerance for i in range(len(actual)) ]):
            print(f"Counterexample: k={k}")
            print(f"Actual: {actual}")
            print(f"Mins: {mins}")



def complete_pairs(k, halves):
    return [ (h, 2*k-h) for h in sorted(halves) ]



set_functions(False, True)
