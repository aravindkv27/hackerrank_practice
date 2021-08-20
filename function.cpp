#include<iostream>
using namespace std;
int max_of_four(int a,int b,int c,int d)
{
  int final=0;
  if(a>b && a>c && a>d)
  {
    final=a;
    cout<<final<<endl;
  }
  else if(b>a && b>c && b>d)
  {
    final=b;
    cout<<final<<endl;
  }
  else if(c>a && c>b && c>d)
  {
    final=c;
    cout<<final<<endl;
  }
  else{
    final=d;
    cout<<final<<endl;
  }
  return 0;
}
int main()
{
  int a,b,c,d;
  cin>>a>>b>>c>>d;
  max_of_four(a,b,c,d);

}
