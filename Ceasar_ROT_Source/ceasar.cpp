#include <iostream>
using namespace std;
 
string encrypt(string text, int s)
{
    string result = "";
 
    for (int i = 0; i < text.length(); i++) {
        if (text[i] == ' ') {
            result += ' ';
            continue;
        }
        if (isupper(text[i]))
            result += char(int(text[i] + s - 65) % 26 + 65);
 
        else
            result += char(int(text[i] + s - 97) % 26 + 97);
    }
 
    return result;
}
 
int main()
{
    string text;
    int s;
    cout << "Text : "; getline(cin, text);
    cout << "Shift: "; cin >> s;
    cout << "Cipher: " << encrypt(text, s);
    return 0;
}