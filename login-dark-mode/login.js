function validateLogin() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var loginStatus = document.getElementById("login-status");

  // Defina um array de usuários e senhas válidos
  var users = [
    { username: "luis", password: "luiscogomes" },
    { username: "joao", password: "senha123" },
    // Adicione mais pares de usuário e senha conforme necessário
  ];

  // Verifique se as credenciais correspondem a um usuário válido
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
