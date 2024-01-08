console.log('> Iniciando o servidor...\n');
const express = require('express');
const path = require('path');
const http = require('http');

const app = express();
const portaNormal = 3000;
const portaAdmin = 1024;


const allowAdminAccess = (req, res, next) => {
    const allowedIPs = ['::ffff:192.168.188.12'];
    const clientIP = req.ip || req.connection.remoteAddress;
    
    if (allowedIPs.includes(clientIP)) {
        next();
    } else {
        res.status(403).send('Acesso proibido');
        console.log(`> Acesso proibido de ${clientIP}`);
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
    console.log(`> Servidor do site normal rodando em http://localhost:${portaNormal}`);
});

serverAdmin.listen(portaAdmin, () => {
    console.log(`> Servidor da área de administração rodando em http://localhost:${portaAdmin}/admin\n`);
});
