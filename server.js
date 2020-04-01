const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors')

app = express()
app.use(cors())
port = 3000;

app.listen(port);

console.log('RESTful API server started on: ' + port);

// middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const routes = require('./routes/appRoutes'); //importing route
routes(app); //register the route