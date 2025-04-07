#include <iostream>
#include <string>

using namespace std;

class RDP {
private:
    string input;
    int index;

    bool match(char expected) {
        if (index < input.size() && input[index] == expected) {
            index++;
            return true;
        }
        return false;
    }

    bool S() {
        // S → ( L ) | a
        if (match('a')) {
            return true;
        } else if (match('(')) {
            if (L() && match(')')) {
                return true;
            }
        }
        return false;
    }

    bool L() {
        // L → S L’
        if (S()) {
            return L_p();
        }
        return false;
    }

    bool L_p() {
        // L’ → , S L’ | ε
        if (match(',')) {
            if (S()) {
                return L_p();
            }
            return false;
        }
        return true; // ε (empty) case
    }

public:
    RDP(string str) {
        input = str;
        index = 0;
    }

    void parse() {
        if (S() && index == input.size()) {
            cout << "Valid string" << endl;
        } else {
            cout << "Invalid string" << endl;
        }
    }
};

int main() {
    string input;
    cout << "Enter a string to validate: ";
    cin >> input;

    RDP parser(input);
    parser.parse();

    return 0;
}
