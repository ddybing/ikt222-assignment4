# Attack 1 

This attack is related to the login form on regjeringen.uiaikt.no. 

The form has a timing vulnerability that allows us to guess the password. 
It does not check the username. 

We were able to find the password by manually brute forcing. We first found the length of the password, 
then tried to replace each character one by one until the number of cycles taken to process the request increased.


We are given a cookie upon successful login. It has a 'authenticated' value, which is set to true.


The solution: 
```
Username: <any>
Password: KattenMinEKul12
```