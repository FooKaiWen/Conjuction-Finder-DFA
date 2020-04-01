document.getElementById('input-file')
    .addEventListener('change', getFile)

function getFile(event) {
    const input = event.target
    if ('files' in input && input.files.length > 0) {
        placeFileContent(
            document.getElementById('content-target'),
            input.files[0])
    }
}

function placeFileContent(target, file) {
    readFileContent(file).then(content => {
        saveDataToFile(content)
        content = content.replace(/(\r\n|\n|\r)/g, "<br />");
        target.innerHTML = content
    }).catch(error => console.log(error))
}

function saveDataToFile(data) {
    var blob = new Blob([data],
        { type: "text/plain;charset=utf-8" });
    saveAs(blob, "static.txt");
}

function readFileContent(file) {
    const reader = new FileReader()
    return new Promise((resolve, reject) => {
        reader.onload = event => resolve(event.target.result)
        reader.onerror = error => reject(error)
        reader.readAsText(file)
    })
}

var Model = function () {
    var self = this;
    self.data = ko.observable({})
    self.stats = ko.observable({})
    self.statsName = ko.observable({})
    self.statsValue = ko.observable({})
    self.uniqueNum = ko.observable(0)
    self.text = ko.observable('')
    self.data.subscribe(function (data) {
        self.text(data['outputText']) ? data['outputText'] : '';
        self.stats(data['outputStats']) ? data['outputStats'] : '';
        self.uniqueNum(data['outputUnique']) ? data['outputUnique'] : '';
    })
    self.stats.subscribe(function (data) {
        self.statsName(Object.keys(data))
        self.statsValue(Object.values(data))
    })
    self.text.subscribe(function (data) {
        data = data.replace(/(\r\n|\n|\r)/g, "<br />");
        var tempDiv = document.createElement('p');
        tempDiv.innerHTML = data;
        var title = document.getElementById("output");
        title.parentNode.insertBefore(tempDiv, title.nextSibling);
        // title.parentNode.appendChild(tempDiv);
    })
};

var model = new Model();
ko.applyBindings(model);

async function getData(url = '', params = {}, returnKo) {
    var url = new URL(url)

    url.search = new URLSearchParams(params).toString();

    fetch(url)
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {
                    returnKo(data)
                });
            }
        )
        .catch(function (err) {
            console.log('Fetch Error :-S', err);
        });
}

async function readText() {
    getData('http://localhost:3000/readtext', {}, model.data)
}

readText()