const controller = require('../controller/controller');


function app(app) {
    app.route('/readtext')
        .get(controller.readtext)
};

module.exports = app