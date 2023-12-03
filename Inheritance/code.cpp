// shift array element at last position but number should shift at right and particular  element should shift at last position
#include <iostream>
#include <cmath>
using namespace std;

bool isTriangularNumber(int num) {
    int calc = 8 * num + 1;
    int squareRoot = sqrt(calc);
    return squareRoot * squareRoot == calc;
}
int main()
{
    int sum=0;
    int n;
    cout << "Enter the size of array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the element of array: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for(int k=0;k<2;k++){
    for (int i = 0; i < 2; i++)
    {
        int temp;
        if (arr[0] < arr[1])
        {
            temp = arr[0];
            for (int j = 0; j < n; j++)
            {
                arr[j] = arr[j + 1];
            }
            arr[n - 1] = temp;
            if(isTriangularNumber(arr[n-1])){
                sum=sum+arr[n-1];
            }
        }
        else if (arr[0] > arr[1])
        {
            temp = arr[1];
            for (int j = 1; j < n; j++)
            {
                arr[j] = arr[j + 1];
            }
            arr[n - 1] = temp;
             if(isTriangularNumber(arr[n-1])){
                sum=sum+arr[n-1];
            }
        }
        else
        {
            temp = arr[0];
            for (int j = 0; j < n; j++)
            {
                arr[j] = arr[j + 1];
            }
            arr[n - 1] = temp;
             if(isTriangularNumber(arr[n-1])){
                sum=sum+arr[n-1];
            }
        }
    }
    }

    cout << "Answer is: " << sum << "\n ";
    
    return 0;
}