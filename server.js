console.clear()
console.log('> Iniciando o servidor...\n')
const express = require('express')
const path = require('path')
const http = require('http')
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');


const app = express()
const portaNormal = 3000

const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutos
    max: 100 // número máximo de requisições permitidas de um IP nesse período
});

app.use(limiter);
app.set('trust proxy', 1);
app.use(helmet());

app.use(express.static(path.join(__dirname, 'public')))
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'))
})

const server = http.createServer(app)

server.listen(portaNormal, () => {
    console.log(`> Servidor do site rodando em http://localhost:${portaNormal}`)
})
