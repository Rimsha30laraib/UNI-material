#include <iostream>
using namespace std;

// Sequential Binary Search
int binarySearch(int arr[], int n, int toSearch)
{
    int low = 0, high = n - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2; // mid calculation
        if (arr[mid] == toSearch)   // check if it is found
        {
            return mid;
        }
        else if (arr[mid] < toSearch) // if the value is less than change the low
        {
            low = mid + 1;
        }
        else // otherwise change the high
        {
            high = mid - 1;
        }
    }
    return -1;
}

int main(int argc, char **argv)
{
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]); // calculate the size of array
    int toSearch;                         // value to search

    cout << "Sequential Binary Search\n";
    cout << "Enter the value you want to search: ";
    cin >> toSearch;
    int result = binarySearch(arr, n, toSearch); // store the result
    if (result != -1)                            // check if value is found or not
    {
        cout << "Found " << toSearch << " at index: " << result << endl;
    }
    else
    {
        cout << "Value not found!" << endl;
    }

    return 0;
}