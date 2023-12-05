# Attack 6 - Finding states secrets

After having signed into the website at https://state-secrets.internal.regjeringen.uiaikt.no/, we were presented with 2 binaries.

`reverse-engineering-debug-bin` and `reverse-engineering-bin`

Upon closer inspection, we saw that these were both Linux executables. 

We firstly tried running the executable to get an overview of what we could expect to see when decompiling.
During opening of the binary, we are presented with a login screen. Testing a random combination shows a split second "login failed" text.

After testing running the file, we then tried to open the executable directly in a text editor in hope to be able to see all the program's strings right away.
We could then see the username `statsminister` and password `erna`.

After finding the credentials, we can confirm that we found the secrets