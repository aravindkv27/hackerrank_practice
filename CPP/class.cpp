#include<iostream>
using namespace std;
class Student{
 public:
  int roll_no;
  string address;
  int phone_no;

};
int main()
{
  Student kv;
  kv.roll_no=19;
  kv.name="Aravind";
  cout<<"Roll_no "<<kv.roll_no<<" and Name "<<kv.name;
}
