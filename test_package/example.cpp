#include <iostream>
#include <gsl/span>

int main(int, char* [])
{
    int arr[4] = {1, 2, 3, 4};
    gsl::span<int> s{&arr[0], 2};
    return 0;
}