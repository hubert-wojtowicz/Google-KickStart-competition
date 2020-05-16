# 12.05.2020
- 300x300 gives 900 000 fields
- 10^5x10^5 gives 1e10 fields
- This number 1e10 is huge...
- let's assume (w,h) means w-column, h-row, where 1 <= w,h <= 10^5
- let's assume we can calculate probability of approaching (w,h) field in rectangle without obstacle by the robot as P(w,h) in O(1)
- if we would be able to find P(w,h), then:
    - we could calculate probability of fail as sum P_fail = P(L,U)+ P(L+1,U) + .. P(R,U) + P(L,U+1) +P(L,U+2)+.. P(L, D), as robot go only right and down
    - we could calculate probabulity of pass as P_pass = 1-P_fail
    - pesimistic operation nuber is O(R-L+D-U) ≈ O(W + H) ≈ O(W)

Let's try to find P(w,h) formula...

P(1,1) = 1
P(2,1) = 0.5
P(3,1) = 0.25
....
P(w,1) = (1/2)^(w-1)

this has symmetry through diagonal:

P(1,1) = 1
P(1,2) = 0.5
P(1,3) = 0.25
....
P(1,h) = (1/2)^(h-1)

Lets imagine you can draw line between fields (k,1) and (1,k), where k <= W and k <= H in the same time. 
Sum of probability of approaching all fields must be equal 1, as it is certain robot will enter one of them.
Lets call such line k-move.

| 1    | .5   | .25  | .125 |   |
| ---  | ---  | ---  | ---  |---|
| .5   |  .5  | .375 |      |   |
| .25  | .375 |      |      |   |
| .125 |      |      |      |   |

there can be general recursion equation provided for this:

P(w,h) = 0.5(P(w, h-1)+P(w-1,h))
with edge conditions:
P(w,1) = (1/2)^(w-1)
P(1,h) = (1/2)^(h-1)

We know also P(w,h) = P(h,w). 

# 13.05.2020

I noticed this is similar pattern to [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).
Lets draw our map indicating number ow ways Q(w,h) we can acheive (w,h):

| 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|
| 1 | 2 | 3 | 4 |   |
| 1 | 3 | 6 |   |   |
| 1 | 4 |   |   |   |
| 1 |   |   |   |   |

There is formula for position Q(w,h)= (h + w -2) over w-1.
For example Q(2,4)= 4 over 1 = 4!/((4-1)!1!) = 4.
There is also property of Pascal's triangle that in k row we have sum exactly equal to 2^k k=w+h-2.
Sooooo... P(w,h) = Q(w,h)/2^(w+h-2) = Q(w,h)/2^(w+h-2).
That's better than recursive equation

To get what we need finally is to calculate sum for P_fail. 
Maybe there will be some analitycal simplification for those as calculating n over k can be also expensive.

I started to analyze sum and I did not noticed any way to simplify this sum... 
I decided to take a hint from google author analysis as I got stucked.

Ok I went too far :D I should think more positive, that's conclusion (calculatin Jemma P_fais :P). But a lot of work was already done. :)

So, there are only two ways(if balck-hole does not touch map border). Jemma can go one of then P_pass = P_go_path1 + P_go_path2.
Convinient way is to calculate sum of probalities that comes out of hole diagioals, as those are rows in Pascal's Triangle.

Lets pick-up k row containing (R,D) point and fields below hole and call id sub-diagonal1 and pick up sub-diagonal2 similarly containing (L,U) fiels. 
Jemma will pass if she will pass sub-diagonal1 or sub-diagonal2.

P(w,h)=(w+h-2 over w-1)/2^(w+h-2)
For simplicity lets use n(w,h)=w+h-2 and k=w-1 => P(w,h) = (n over k) /2^n.

This hint I also took from task analysis - use log2x representation to avoid storing great nubers.
P(w,h) = 2^log_2((n over k) /2^n), so:
P(w,h) = 2^(log_2(n!)-log_2((n-k)!)-log_2(k!)-n)

we can calculate upfront log_2(0!), log_2(1!), log_2(2!),.., log_2((w+h-2)!) and in constant time calculate P(w,h).

log_2(t!) = log_2((t-1)!)+log_2(t)
log_2(1!) = 0
log_2(0!) = 0

Finally:
P(w,h) = 2^lg((w+h-2)!)-lg((w-1)!)-lg((h-1)!)-w-h+2} when h>=1 and w>=1
