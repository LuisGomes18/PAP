function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var loginStatus = document.getElementById("login-status");
  
    if (username === "luis" && password === "luiscogomes") {
      loginStatus.innerHTML = "Login bem-sucedido!";
      window.location.href = "home.html"; // Redirecionar para a página home
    } else {
      loginStatus.innerHTML = "Credenciais inválidas. Tente novamente.";
    }
  }
  