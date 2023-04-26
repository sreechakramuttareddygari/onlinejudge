 #include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int count=0;
    //cout<<n<<" ";
    double sq_n = sqrt(n);
    for(int i=1;i<=sq_n;i++){
    if(i*i<=n){
    count++;
}
}
cout<<count;
}