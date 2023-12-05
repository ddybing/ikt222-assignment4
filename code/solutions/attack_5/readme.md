# Attack 5 - Uploading files to Dropbox


As mentioned in the previous attack, we were given a Dropbox link.


This link is https://dropbox.internal.regjeringen.uiaikt.no/




The site is used to upload files to the Dropbox folder of user 'ingridnilsen'.

However, when inspecting the upload request, there is a _filename_ variable in the request, which can be changed.  

The server does not sanitize the filename, and treats it as a filepath. 
This means that we choose where the file is stored, by prefixing the filename with e.g. '../'.



During sending of a file, we had a look in the network tab in inspect element. There we then altered the raw upload data, changing the filename to `../filename.txt` proved that the file did indeed get uploaded in the parent folder being `/home/ingridnilsen/dropbox/filename.txt` instead of `/home/ingridnilsen/dropbox/upload/filename.txt`.

With this knowledge in mind, we now crafted our `authorized_keys` file to be uploaded to the server. The upload filename was altered to `../../.ssh/authorized_keys`. This resulted in the file being stored the filepath `/home/ingridnilsen/.ssh/authorized_keys`.

Now trying to login to the previous scanned SSH servers in the [attack_4](/code/solutions/attack_4) solution, we were able to successfully sign in to `10.13.13.253` using `ssh ingridnilsen@10.13.13.253`.

After signing in, looked around the directories and found `level3_secrets.txt` located in `/home/ingrid.nilsen/level3_secrets.txt`. In this file we found the credentials needed to sign in to https://state-secrets.internal.regjeringen.uiaikt.no/


