function signup() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            email: email,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        // if (data.message) {
        //     window.location.href = "/login";
        // }
        window.location.href = "/login";
    })
    .catch(err => console.error(err));
}
