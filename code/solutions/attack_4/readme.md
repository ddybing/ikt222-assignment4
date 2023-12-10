# Attack 4

This attack requires a wireguard connection to server with address `64.225.76.73`. When connected, it should give you access to the subnet of `10.13.13.0/24`

After connecting to wireguard, you can start the attack by sending in an unexpected length in the login form located at `http://10.13.13.254/login`. The script sends in a string of 1s 512 times. The information then gets printed in the terminal.
