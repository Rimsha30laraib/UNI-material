binary search:
#include <iostream>
#include <mpi.h>
using namespace std;

void mpiBinarySearch(int argc, char** argv, int arr[], int n, int key) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int chunkSize = n / size;
    int start = rank * chunkSize;
    int end = (rank == size - 1) ? (n - 1) : (start + chunkSize - 1);

    // Show which part this process is responsible for
    cout << "Process " << rank << " searching indices [" << start << ", " << end << "]" << endl;

    int foundIndex = -1;
    for (int i = start; i <= end; i++) {
        if (arr[i] == key) {
            foundIndex = i;
            break;
        }
    }

    if (foundIndex != -1) {
        cout << "Process " << rank << " found the number at index " << foundIndex << endl;
    }

    // Use MPI_Reduce to get the max index (i.e., valid index if found)
    int globalIndex = -1;
    MPI_Reduce(&foundIndex, &globalIndex, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        cout << "\nFinal Result: ";
        if (globalIndex != -1)
            cout << "Key " << key << " found at index: " << globalIndex << endl;
        else
            cout << "Key " << key << " not found in array." << endl;
    }

    MPI_Finalize();
}

int main(int argc, char** argv) {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 13;  // You can change this or take from user input

    mpiBinarySearch(argc, argv, arr, n, key);
    return 0;
}