#include<iostream>

using namespace std;

int BinarySearch(int arr[],int value,int max_index)
{
	int min_index =0;

	while(true)
	{
		while(min_index<max_index)
		{


			int mid_index = (min_index + max_index)/2;
			if(arr[mid_index] == value)
			{
				return mid_index;
			}
			else
			{
				if(value > arr[mid_index])
				{
					min_index = mid_index;
				}
				else
				{
					max_index = mid_index;
				}
			}
			
			


		}
	}


}

int main()
{
	cout<<"your data must be sorted to perform binary search on it."<<endl;
	cout<<"I am cosidering the data is sorted in ascending order."<<endl;
	cout<<"complexity for binary search is O(log n)."<<endl;

	int arr[] = {0,1,2,3,4,5,6,7,8,9,10};

	cout<<"enter the value to be found : ";
	int target;
	cin>>target;
	int max_index = sizeof(arr)/sizeof(int);
	int x = BinarySearch(arr,target,max_index);

	cout<<"the value is present at index : "<<x;

	
}
