#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

// Helper function to check if a vector is sorted in ascending or descending order
bool is_sorted(const vector<int>& lst) {
    return is_sorted(lst.begin(), lst.end()) || is_sorted(lst.rbegin(), lst.rend());
}

// Helper function to check if all adjacent elements have differences between 1 and 3
bool has_valid_differences(const vector<int>& lst) {
    for (size_t i = 0; i < lst.size() - 1; ++i) {
        if (abs(lst[i] - lst[i + 1]) < 1 || abs(lst[i] - lst[i + 1]) >= 4) {
            return false;
        }
    }
    return true;
}

// Check if a vector is safe according to the original rules
bool is_safe(const vector<int>& lst) {
    return is_sorted(lst) && has_valid_differences(lst);
}

// Check if a vector can become safe by removing one element
bool can_be_safe_by_removal(const vector<int>& lst) {
    for (size_t i = 0; i < lst.size(); ++i) {
        vector<int> modified_list = lst;
        modified_list.erase(modified_list.begin() + i); // Remove the i-th element
        if (is_safe(modified_list)) {
            return true;
        }
    }
    return false;
}

// Main function to check safe reports
int safe_data_check(const string& raw_data) {
    vector<vector<int>> check_list;
    istringstream stream(raw_data);
    string line;

    // Parse the raw data into a 2D vector
    while (getline(stream, line)) {
        istringstream line_stream(line);
        vector<int> temp;
        int num;
        while (line_stream >> num) {
            temp.push_back(num);
        }
        check_list.push_back(temp);
    }

    int safe_report = 0;

    // Check safety conditions for each list
    for (const auto& lst : check_list) {
        if (is_safe(lst) || can_be_safe_by_removal(lst)) {
            ++safe_report;
        }
    }

    return safe_report;
}

// Main driver function
int main() {
    string raw_data = R"(7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9)";

    int result = safe_data_check(raw_data);
    cout << result << endl; // Output: 4

    return 0;
}
