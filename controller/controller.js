var model = require('../model/model');

exports.readtext = function (req, res) {
  model.readtext(function (err, data) {
    console.log('Read file at ' + new Date())
    if (err)
      res.send(err);
    res.json(data);
  });
};