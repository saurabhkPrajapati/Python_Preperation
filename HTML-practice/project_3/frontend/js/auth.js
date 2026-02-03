function authFetch(url) {
    const access_token = localStorage.getItem("access_token");
    console.log("TOKEN sent:", access_token);

    if (!access_token) {
        throw new Error("No access_token found");
    }

    return fetch(url, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${access_token}`,
        }
    });
}

function loadUserData() {
    const result = document.getElementById("result");

    authFetch("http://127.0.0.1:5000/user")
        .then(res => res.json())
        .then(data => {
            result.innerText = data.message || data.error;
        })
        .catch(err => {
            result.innerText = err.message;
            console.error(err);
        });
}

function logOut() {
    localStorage.removeItem("access_token");
    window.location.href = "/login";
}
