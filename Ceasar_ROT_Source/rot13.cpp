#include<bits/stdc++.h>
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

string decrypt(string text, int s)
{
    return encrypt(text, 26 - s);
}

int main()
{	
	string message;
    cout << "Encoded Text : "; getline(cin, message);
	int shift = 13;
	
	cout << encrypt(message, shift) << "\n";

    cout << "Decoded Text : "; getline(cin, message);
	
	cout << decrypt(message, shift) << "\n";
	
	return 0;
}
