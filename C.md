#д��ǰ��
һ�����C�Ľ��鿩��Ҳ����C++

----

## ����Dev C++

* ��ʱ��ᷢ�����˴��뵫���������Ǿɰ汾���������Ҫ����Ƿ�ر����������е�exe������ǹ�����Ҫ��F12ȫ�����±�����ջ���

* ���빤�̴���λ��Makefile˵���к��������˵�û�ж���

* �������ֻ��Ҫ����C��Ϊ׷������ٶȿ��Կ���ʹ��tcc (Tiny C Compile)���������μ�https://qs1401.com/?post=18

----

## ���������

�ҽ������е�����ȫ��ʹ��gets��ɣ�Ȼ������sscanf��ȡ������

��Ȼ����ȫ����fgets(buf,9999,stdin);

���´�����ʾ�������뷽�����������n��������qsort���������ʽ����һ�� N��ʾ���ĸ������ڶ��� N����Ҫ�������(N<1000)

```C
#include <stdio.h>
#include <stdlib.h>
char buf[9999];
int data[1005]; //��Ҫ�ھֲ�������������飬��ըջ
int cmp(const void* a,const void* b){
    return *(int*)a-*(int*)b;
}
int main(){
    int N,i;
    gets(buf);
    sscanf(buf,"%d",&N);
    gets(buf);
    for(i=0;i<N;i++) {
        sscanf(buf,"%d %[^\n]",&data[i],buf);
    }
    qsort(data,N,sizeof(int),cmp);
    for(i=0;i<N-1;i++) printf("%d ",data[i]);
    printf("%d",data[i]);
}
```

----
## C++��sstream����sprintf

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