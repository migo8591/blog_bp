setTimeout(function() {
    document.getElementById("flash-message").style.display = "none";
}, 3000);

document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const loginSuccess = urlParams.get("login_success");
    if (loginSuccess === "True") {
        alert("¡Bienvenido!");
    }
});