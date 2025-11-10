#include <bits/stdc++.h>
using namespace std;

void printInput(vector<int> &p, vector<int> &w) {
    cout << "\nItems (Profit | Weight)\n";
    cout << "+----------+----------\n";

    for (int i = 0; i < p.size(); i++) {
        cout << setw(10) << left << p[i] << "|"
             << setw(10) << left << w[i] << "|\n";
    }
    cout << endl;
}

int main() {
    int n, cap;

    cout << "Enter number of items: ";
    cin >> n;

    vector<int> p(n), w(n);

    for (int i = 0; i < n; i++) {
        cout << "\nProfit of item " << i + 1 << ": ";
        cin >> p[i];
        cout << "Weight of item " << i + 1 << ": ";
        cin >> w[i];
    }

    cout << "\nEnter capacity: ";
    cin >> cap;

    printInput(p, w);

    vector<vector<int>> dp(n + 1, vector<int>(cap + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int c = 1; c <= cap; c++) {
            if (w[i - 1] <= c) {
                dp[i][c] = max(
                    p[i - 1] + dp[i - 1][c - w[i - 1]],
                    dp[i - 1][c]
                );
            } else {
                dp[i][c] = dp[i - 1][c];
            }
        }
    }

    cout << "\nDP Table:\n";
    for (int i = 0; i <= n; i++) {
        for (int c = 0; c <= cap; c++) {
            cout << setw(5) << dp[i][c] << " ";
        }
        cout << endl;
    }

    cout << "\nMaximum Profit (0/1 Knapsack): "
         << dp[n][cap] << endl;

    return 0;
}
