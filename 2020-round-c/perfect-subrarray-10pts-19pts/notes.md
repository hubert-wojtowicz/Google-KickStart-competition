# Task theory
- notice relation `sum(A[L...R]) = sum(A[0...R]) - sum(A[0...L-1])` for `0 < L <= R <= N`
- lets define `Sk = k*k` for `k >= 0` called perferct square
- we need to remember to take into account `A[0]` if `k` exist, that` A[0] == Sk`
- we can precalculate `sum(A[0...i])`, `i = 0,1,..,N` and keep in memory
- can also remember assigment `P: P(sum_value) -> count`, as `sum_value` belongs to finit range of `[-10^7;10^7]` numbers
- such big range for `P` can be represented as `defaultdict(lambda: 0)` in python3 (collections.defaultdict) to avoid redundand memory consumption 
- what we looking for is all solutin of: <br>
    `sum(A[L...R]) = Sk, k>=0, 0 <= L <= R <= N`
- For the curren iteration `i = 1,..,N` we need to find all `k` and `L` that solves equation with constrains `k >= 0`, `0 < L <= i`:<br>
    `Sk = sum(A[L...R]) = sum(A[0...R]) - sum(A[0...L-1])`, if `R=i`:<br>
    `sum(A[0...L-1]) = sum(A[0...i]) - Sk` 
- we know current value of `sum(A[0...i])` for `i` iteration as we store it in memory
- using `P(sum(A[0...i]) - Sk)` we can fastly verify (dictionary access `O(1)`) how much `sum(A[L...i]) = Sk` exists
- we can notice, we need chceck only `Sk`:<br>
    `min(sum(A[0...L-1])) <= sum(A[0...i]) - Sk`, so: <br>
    `Sk <= sum(A[0...i]) - min(sum(A[0...L-1]))`, what is equivalent to:<br>
    `0 <= Sk <= sum(A[0...i]) - min(sum(A[0...i-1]))`, solving that inequality for provided `i` we can reason set of `k` collection
- using that restricted `k` collection we can find all possible contigious sum ending at i-index being sum of perfect square
- we sum number of `P(sum(A[0...i]) - Sk)` for each `i=1,..,N` for resolved from ineqation `k`, this way we get answer to test set

# Implementation language
This was first time when I was unable to provide solution in python as it appeared too slow. Thanks to more control over memory allocation I provide solution in C++ language. Maybe this is the sign to switch to this language. 