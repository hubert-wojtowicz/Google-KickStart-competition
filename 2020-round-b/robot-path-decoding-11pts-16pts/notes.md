# Notes
- Movements sequence order does not matter i.e WWWWWS ≡ 5(W)S ≡ S5W.
- Soubroutine can be simplified 4(W2(S)) ≡ 4(W)8(S).
- Programs subroutine can be represented on stack data structure.
- Stack will simplify parsing brackets.
- Alternative to explicite stack is recursion (runtime callstack).
- Max length of program is 2000 characters. For test set 1 only 10^4 movements out of such program can be moved. 
I can imagine 2000 characters program in test set 2
9(9(... (9W)...)) 
having 9E667 moves (3*k+2=2000 => k=666).
- in the first place I wan put on stack multiplier, but I realized it will grow expotentialy to value from range [1, 9E667]. Then I ralized it will be better to put subprogram movement on stack as this value belongs to range [1,10E9] due to limited map space and can be easily sored in memory.