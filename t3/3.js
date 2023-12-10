'use strict';

var names = ['John', 'Paul', 'Jones'];

var ulElement = document.getElementById('target');

var htmlContent = '';

for (var i = 0; i < names.length; i++) {
    htmlContent += '<li>' + names[i] + '</li>';
}

ulElement.innerHTML = htmlContent;