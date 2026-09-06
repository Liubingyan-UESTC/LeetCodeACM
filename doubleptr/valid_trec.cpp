#include<iostream>
#include <string>
#include <vector>

using namespace std;

int valid_trec_of_k(string str , int n , int k){
    vector<int> st;
    long long res = 0;
    
    for(int i = 0 ; i < n ; ++i){
        if (str[i] == '('){
            st.push_back(i);
        } else {
            int l = st.back();
            st.pop_back();
            int len = i - l - 1;
            if (len % k == 0){
                ++res;
            }
        }
    }
    cout << res << '\n';
    return res;
}

int main(){
    int n , k;
    cin >> n >> k;
    
    string str;
    cin >> str;

    int l = 0 , r = 0;
    
    int res = valid_trec_of_k(str , n, k);

}
