#include <bits/stdc++.h>
using namespace std;

void printTable(vector<vector<float>> &v, bool isResult) {
    cout << setw(10) << left << "Profit|"
         << setw(10) << left << "Weight|";

    if (isResult)
        cout << setw(10) << left << "Frac|";
    else
        cout << setw(10) << left << "P/W|";

    cout << "\n+----------+----------+----------\n";

    for (auto &x : v) {
        cout << setw(10) << left << x[1] << "|"
             << setw(10) << left << x[2] << "|"
             << setw(10) << left << x[0] << "|\n";
    }
    cout << endl;
}

void inputItems(vector<vector<float>> &v, int &n, float &cap) {
    cout << "Enter number of items: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        float p, w;
        cout << "\nProfit of item " << i + 1 << ": ";
        cin >> p;
        cout << "Weight of item " << i + 1 << ": ";
        cin >> w;

        float pw = p / w;

        v.push_back({pw, p, w});
    }

    cout << "\nEnter capacity: ";
    cin >> cap;
}

int main() {
    vector<vector<float>> v;
    int n;
    float cap;

    inputItems(v, n, cap);

    cout << "\nEntered Items:\n";
    printTable(v, false);

    sort(v.begin(), v.end());   // ascending by ratio

    vector<vector<float>> res = v;

    float profit = 0;

    for (int i = n - 1; i >= 0; i--) {
        float pw = v[i][0];
        float p  = v[i][1];
        float w  = v[i][2];

        if (w <= cap) {
            cap -= w;
            profit += p;
            res[i][0] = 1;     // full item
        } 
        else {
            float frac = cap / w;
            profit += p * frac;
            res[i][0] = frac;  // fractional part
            cap = 0;
            break;
        }
    }

    cout << "\nFinal Result:\n";
    printTable(res, true);

    cout << "Total Profit: " << profit << endl;
}
