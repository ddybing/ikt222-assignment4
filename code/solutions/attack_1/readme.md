# Attack 1 

In this attack we perform a (simulated) timing attack.
The server will give us the response of how many cycles was performed to check the password.

The python script we write first figures out the length of the password, then it starts from left to right to insert the correct characters, based of the timing information returned in the response. For each correct character, the timing will go up by 1.

Finally once we get the `set-cookie` header, we know the password is correct.

2 things to note in this attack. The username is not checked, neither for being set, nor its value. The other thing to note is that it doesn't matter what the last character of the password is.

The solution: 
```
Username: <any>
Password: KattenMinErKul123
```
