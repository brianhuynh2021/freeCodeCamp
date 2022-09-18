var http = require('http');
var dt = require('./my_module')

http.createServer((req, res) => {
    res.writeHead(200, {'Content-type': 'text/html'});
    res.write('The date and time are currently: ' + dt.myDateTime());
    res.end('\nHello World!');
}).listen(8080);