#include <bits/stdc++.h>
using namespace std;

void printBoard(vector<vector<int>> &b, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << (b[i][j] ? "Q " : ". ");
        cout << endl;
    }
    cout << endl;
}

bool isSafe(vector<vector<int>> &b, int r, int c, int n) {
    for (int i = 0; i < c; i++)
        if (b[r][i]) return false;

    for (int i = r, j = c; i >= 0 && j >= 0; i--, j--)
        if (b[i][j]) return false;

    for (int i = r, j = c; i < n && j >= 0; i++, j--)
        if (b[i][j]) return false;

    return true;
}

bool solve(vector<vector<int>> &b, int c, int n) {
    if (c == n) {
        printBoard(b, n);
        return true;
    }

    bool ok = false;

    for (int r = 0; r < n; r++) {
        if (isSafe(b, r, c, n)) {
            b[r][c] = 1;
            ok = solve(b, c + 1, n) || ok;
            b[r][c] = 0;
        }
    }
    return ok;
}

int main() {
    int n;
    cout << "Enter size of chessboard (N): ";
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n, 0));

    if (!solve(board, 0, n))
        cout << "No solution exists for " << n << "-Queens problem.\n";

    return 0;
}
