#д��ǰ��
һ�����C�Ľ��鿩��Ҳ����C++

----
#C++��sstream����sprintf

```cpp
#include <string>
#include <sstream>
#include <iostream> 
using namespace std;
int main(){
    stringstream s;
    string result;
    int i = 1000;
    s <<"haha"<< i; 
    s >> result; 
    cout << result << endl; // print "haha1000"
    s.clear();
} 
```