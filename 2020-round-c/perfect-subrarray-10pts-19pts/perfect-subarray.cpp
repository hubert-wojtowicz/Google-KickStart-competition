#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int nmax = 1e5;
const int maxsum = nmax * 100;
int A[nmax], P[2 * 100 * nmax + 1];

void testCase()
{
    int N, lminsum = 0, lmaxsum = 0, s = 0;
    long long res = 0;
    cin >> N;
    for (int n = 0; n < N; ++n)
    {
        cin >> A[n];
        if (A[n] < 0)
            lminsum += A[n];
        else
            lmaxsum += A[n];
    }

    ++P[-lminsum];
    for (int i = 0; i < N; ++i)
    {
        s += A[i];
        if (lminsum > s)
            lminsum = s;
        for (int k = 0; k * k <= s - lminsum; ++k)
        {
            res += P[s - k * k - lminsum];
        }
        ++P[s - lminsum];
    }
    cout << res << "\n";
    memset(P, 0, sizeof(int) * (lmaxsum - lminsum + 1));
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        testCase();
    }
    return 0;
}
