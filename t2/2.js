var items = ['First item', 'Second item', 'Third item'];

var ulElement = document.getElementById('target');

items.forEach(function (item, index) {
    var liElement = document.createElement('li');

    liElement.textContent = item;

    if (index === 1) {
        liElement.classList.add('my-item');
    }

    ulElement.appendChild(liElement);
});