function ready(fn) {
    if (document.readyState != 'loading'){
        fn();
    } else {
        document.addEventListener('DOMContentLoaded', fn);
    }
}

function onLoad () {
    rollcall();     // variabling all the DOM elements

    elementsList.addEventListener('change', (function() {
        var curSelType = this.selectedOptions[0]
        Element.type = getData(curSelType, 'eltype');
    }))

    UI.errorDiv.style.display = 'none';
}


function queryHandler (data) {
    console.log(data);
}

function sendStuff(query){
    var request = new XMLHttpRequest();
    request.open('POST', '/r', true);


    request.onerror = function() {
        console.log('An error had managed to occure!')
    };

    request.setRequestHeader('Content-Type',
                             'application/json; charset=UTF-8');
    request.send(JSON.stringify(query));

    request.onload = function() {
        if (this.status >= 200 && this.status < 400) {
            var data = JSON.parse(this.response);

            queryHandler(data);
        
        } else {
        console.log("Oh. noes! The Servant went mad with "
                     + this.status + " error!")
        }
    };
}

function rollcall () {
    var elementsList = document.getElementById('elementsList');
    UI.errorDiv = document.getElementById('error');
}

var Element = {};
Element.type = '-1';

Element.Create = function(){

    if(this.type === '-1') {
        UI.Error('Не выбрал тип элемента, ниггер');
        return;
    } else {
        newName = document.getElementById('nameTag').value;
        if (newName === "") {
            UI.Error('Не указал имя, ниггер');
            return;
        }

        var parent = document.getElementsByClassName('selected')[0];
        var parentTag = (parent == undefined)?
                            ('root'):
                            (getData(parent, 'tag'))
        var query = {'requesst': 'createNewElement',
                     'attr': {
                        'name': newName,
                        'parent': parentTag,
                        'type': this.type
                     }}

        sendStuff(query);
        return;
    }
}

var UI = {};
UI.Error = function(text) {
    this.errorDiv.textContent = text;
    this.errorDiv.style.display = '';
}

function getData (el, tag) {
    var attr = el.attributes['data-'+tag]
    if (attr !== undefined) {
        return attr.value;
    } else {
        return null;
    }
}

ready(onLoad);