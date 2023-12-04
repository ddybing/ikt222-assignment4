# Attack 2 


This is related to the the inner portal login form on regjeringen.uiaikt.no. 

This form does check the username.

The password input field is vulnerable to SQL injection attacks, which could be used to extract information from the database that we should otherwise not be able to access.



The solution to the SQL injection is:

```
Username: jonas.dahl

Password: ' OR 1 = 1 OR '
```

This gives us access to "Intranett: Level 1", as the user Jonas Dahl.

The "Intranett: Level 1" website gives us a session cookie, which has the 'httponly' flag set. This means that it is not accessible by any script. 
