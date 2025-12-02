#include <iostream>
#include <omp.h> // For OpenMP parallel implementation
using namespace std;

void parallelBinarySearch(int arr[], int n, int queries[], int qCount, int results[]) {
    #pragma omp parallel for
    for (int i = 0; i < qCount; i++) {
        int low = 0, high = n - 1;
        int key = queries[i];
        results[i] = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == key) {
                results[i] = mid;
                break;
            } else if (arr[mid] < key) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);

    int queries[] = {3, 15, 19, 4};
    int qCount = sizeof(queries) / sizeof(queries[0]);
    int results[qCount];

    parallelBinarySearch(arr, n, queries, qCount, results);

    for (int i = 0; i < qCount; i++) {
        if(results[i]!=-1){
        cout << "Query " << queries[i] << " found at index: " << results[i] << std::endl;
        }
        else{
            cout<<"Query " << queries[i] <<" not found!"<<endl;
        }
    }

    return 0;
}