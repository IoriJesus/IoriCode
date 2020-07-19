#include <iostream>
#include <vector>
#include<string>
 
using namespace std;
 
int main()
{
    vector<int> valores{};
    string mensajeclave;
    
    cin>>mensajeclave;
    
    for(int i=0; i<mensajeclave.size();i++){
    
    if(mensajeclave[i] == '.' )
    valores.push_back(0); 
    
    if(mensajeclave[i] == '-' and mensajeclave[i+1] == '.'){
       valores.push_back(1);  
       i++;
    }
    
    if(mensajeclave[i] == '-' and mensajeclave[i+1] == '-'){
       valores.push_back(2); 
       i++;
    }
    
    }
    
    for(int i=0; i<valores.size();i++){
        cout<<valores[i];
    }
    
    return 0;
}
