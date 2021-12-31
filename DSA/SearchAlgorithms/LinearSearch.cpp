#include<iostream>

using namespace std;

int LinearSearch(int arr[],int value,int length)
{
	
	for(int i=0;i<length;i++)
	{
		if(arr[i]==value)
		{
			cout<<"value found at index ";
			return i;
		}

		
	}
	cout<<"target value i not in the data.";
	return -1;
}

int main()
{
	int arr[]={1,2,3,4,5,6,7,8,9,0};
	int target;
	cout<<"Enter the value to be found ";
	cin>>target;
	int l=sizeof(arr)/sizeof(int);
	cout<<LinearSearch(arr,target,l)<<endl;
}
