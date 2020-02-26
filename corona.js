const die = document.querySelector(".die");
const infected = document.querySelector(".infected");
const restore = document.querySelector(".restore");
const sus = document.querySelector(".sus");
function getData() {
    fetch("http://127.0.0.1:5000/corona"
    ).then(function (response) {
        return response.json();
    }).then(function (json) {
        die.innerHTML = `<p>${json.die}</p>`;
        infected.innerHTML = `<p>${json.infected}</p>`;
        restore.innerHTML = `<p>${json.restore}</p>`;
        sus.innerHTML = `<p>${json.sus}</p>`;
    })
}

function init() {
    getData();
    setInterval(getData, 1000);
}

init();