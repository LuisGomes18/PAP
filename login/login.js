function validateLogin() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var loginStatus = document.getElementById("login-status");

  var users = [
    { username: "luis", password: "luiscogomes" },
    { username: "ColorAD", password: "ColorAD" },
  ];

  var isValidUser = users.some(function (user) {
    return user.username === username && user.password === password;
  });

  if (isValidUser) {
    loginStatus.innerHTML = "Login bem-sucedido!";
    window.location.href = "../home/index.html";
  } else {
    loginStatus.innerHTML = "Credenciais inválidas. Tente novamente.";
  }
}

document.getElementById("login-form").addEventListener("submit", function (e) {
  e.preventDefault();
  validateLogin();
});
