var fs = require('fs')
path = require('path')
// filePath = path.join(__dirname, 'start.html');

filePath = 'output.json'
var model = function(){}

model.readtext = function (result) {
    fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
        if (err) {
            console.log("Error: ", err);
            result(null, err);
        }
        else {
            result(null, JSON.parse(data));
        }
    });
};

module.exports = model;