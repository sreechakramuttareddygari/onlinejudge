 #include <bits/stdc++.h>
using namespace std;

int recurse(string& s, int i,vector<string>& ref,vector<string>& ret,int count){
        if(i==s.size() || count>4)
        {   ref.push_back(s.substr(i));
            bool b=true;
            for(int i=0;i<ref.size();i++){
                if(ref[i].size()>3)
                {b=false;
                break;}
                if(stoi(ref[i])<10 && ref[i].size()>1)
                {b=false;
                }
                if(stoi(ref[i])<100 && ref[i].size()>2)
                {b=false;
                }
                if(stoi(ref[i])>255)
                {b=false;
                //cout<<stoi(ref[i])<<" ";
                }
            }
            if(b){
                string a = ref[0];
            for(int i=1;i<ref.size();i++){
                a+='.'+ref[i];
            }
            ret.push_back(a);
             //cout<<"\n";
             }
            ref.pop_back();
            return 0;
        }
        for(int j=1;j<min((int)s.size()-i,4);j++){
            ref.push_back(s.substr(i,j));
            //cout<<s.substr(i,j)<<" "<<i<<" "<<j<<"\n";
            recurse(s,i+j,ref,ret,count+1);
            ref.pop_back();
        }
        return 0;

    }
    vector<string> restoreIpAddresses(string s) {
        vector<string> ref;
        vector<string> ret;
        recurse(s,0,ref,ret,0);
        return ret;
    }
    int main(){
        string s;
        cin >> s;
        vector<string> ret = restoreIpAddresses(s);
        if(ret.size()==0)
        {cout<<"";
      return 0;}
        cout<<ret[0];
        for(int i=1;i<ret.size();i++){
          cout<<" "<<ret[i];
        }
    }
