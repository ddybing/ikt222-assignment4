# Attack 4





This is the configuration we used for connecting to WireGuard


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


The JSON response when logging in with password as "1111111111111111111..." on the supervisor access login page.

```
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