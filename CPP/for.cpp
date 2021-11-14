#include<iostream>
using namespace std;
int main()
{
  int i,num1,num2;
  string s[]={"one","two","three","four","five","six","seven","eight","nine"};
  cin>>num1>>num2;
  for(i=num1;i<=num2;i++)
  {
    if(i<=9)
    {
      cout<<s[i-1]<<endl;
    }
    else if(i%2==0)
    {
      cout<<"even"<<endl;

    }
    else{
      cout<<"odd"<<endl;
    }
  }
  return 0;
}
