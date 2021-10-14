import textwrap

def wrap(string, max_width):
    tet=textwrap.wrap(string,width=max_width)
    l=len(tet)
    ans=''
    for i in range(0,l):
        ans=ans+tet[i]+'\n'
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result=wrap(string, max_width)
    print(result)