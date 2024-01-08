console.log('> Iniciando o servidor...\n');
const express = require('express');
const path = require('path');
const http = require('http');

const app = express();  // Instância para o servidor do site normal

const portaNormal = 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const server = http.createServer(app);

server.listen(portaNormal, () => {
    console.log(`> Servidor do site normal rodando em http://localhost:${portaNormal}`);
});

