 var targetElement = document.getElementById('target');

    var htmlCode = '<li>First item</li>' +
                   '<li>Second item</li>' +
                   '<li>Third item</li>';

    targetElement.innerHTML = htmlCode;

    targetElement.classList.add('my-list');