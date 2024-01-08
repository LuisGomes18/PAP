console.log('Iniciando o servidor...');
const express = require('express');
const path = require('path');
const http = require('http');

const app = express();
const portaNormal = 3000;
const portaAdmin = 200;

// Middleware para permitir acesso apenas a IPs específicos
const allowAdminAccess = (req, res, next) => {
    const allowedIPs = ['127.0.0.1', '192.168.1.1']; // Substitua pelos IPs desejados
    const clientIP = req.ip || req.connection.remoteAddress;
    
    if (allowedIPs.includes(clientIP)) {
        // IP permitido, continue para a próxima rota
        next();
    } else {
        // IP não permitido, envie uma resposta proibida (403)
        res.status(403).send('Acesso proibido');
    }
};

app.use('/admin', allowAdminAccess);

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin.html'));
});

const serverNormal = http.createServer(app);
const serverAdmin = http.createServer(app);

serverNormal.listen(portaNormal, () => {
    console.log(`Servidor do site normal rodando em http://localhost:${portaNormal}`);
});

serverAdmin.listen(portaAdmin, () => {
    console.log(`Servidor da área de administração rodando em http://localhost:${portaAdmin}/admin`);
});
