#include<bits/stdc++.h>
using namespace std;

unordered_map<int, bool> acceptState;
unordered_map<string, int> transitionTable;

bool isValid = false;


void solve(string & inputString, int state, int idx){
    if(idx == inputString.length()){
        if(acceptState[state]){
            isValid = true;
        }
        return;
    }

    string tr = to_string(state);
    tr += "_";
    tr += inputString[idx];

    int ns = transitionTable[tr];
    solve(inputString, ns, idx+1);
}


int main(){
    int inputCount, stateCount, acceptCount, initialState;
    cout<<"Number of Input Symbols: ";
    cin >> inputCount;

    cout<<"Input symbols: ";
    vector<char> inputSymbols(inputCount);
    for(int i=0; i<inputCount; i++){
        cin >> inputSymbols[i];
    }

    cout<<"Enter number of states: ";
    cin>>stateCount;

    cout<<"Enter Initial State: ";
    cin>>initialState;


    cout<<"Number of accepting states: ";
    cin>>acceptCount;

    cout<<"Accepting States: ";
    for(int i=0; i<acceptCount; i++){
        int s;
        cin>>s;
        acceptState[s] = true;
    }

    cout<<"Transition Table\n";
    for(int i=1; i<=stateCount; i++){
        for(int j=0; j<inputCount; j++){
            string tr = to_string(i);
            tr += '_';
            tr += inputSymbols[j];

            int ns;
            cout<<i<<" to "<<inputSymbols[j]<<" = ";
            cin>>ns;
            transitionTable[tr] = ns;
        }
    }

    string inputString;
    cout<<"Input String: ";
    cin>>inputString;

    solve(inputString, initialState, 0);

    if(isValid){
        cout<<"Valid"<<endl;
    }
    else{
        cout<<"Invalid"<<endl;
    }
}
