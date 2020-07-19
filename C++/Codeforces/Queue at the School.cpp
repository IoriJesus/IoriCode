#include <vector>
#include <iostream>
 
using namespace std;
 
int main(){
	
    vector <char> fila{};
    char letras=' ';
    int n=0,mov=0;
    
    cin>>n;  cin>>mov;
    
    for(int i=0; i<n; i++){
        cin>>letras;
        fila.push_back(letras);
    }
    
    for(int j=0;j<mov;j++){
        for(int i=0; i < n; i++){
         
         if(fila[i]=='B'){
		 
            if(fila[i+1] == 'G'){
	        swap(fila[i],fila[i+1]);
	        i=i+1;
            }
         }
        }
    }
    
    for(int i=0; i<n; i++) cout<<fila[i];
    
    return 0;
}
