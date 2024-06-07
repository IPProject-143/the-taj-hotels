const roomtype = document.querySelector(".room");

if (roomtype.options[roomtype.selectedIndex].text == "Normal room") {
  for (let i = 1; i <= 4; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".adults").appendChild(opt);
  }
  for (let i = 0; i <= 2; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".kids").appendChild(opt);
  }
} else if (roomtype.options[roomtype.selectedIndex].text == "VIP Room") {
  for (let i = 1; i <= 4; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".adults").appendChild(opt);
  }
  for (let i = 0; i <= 2; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".kids").appendChild(opt);
  }
} else if (roomtype.options[roomtype.selectedIndex].text == "Couple's room") {
  for (let i = 2; i <= 4; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".adults").appendChild(opt);
  }
  for (let i = 0; i <= 2; i++) {
    let opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    document.querySelector(".kids").appendChild(opt);
  }
}

function datediff(first, second) {
  return Math.round((second - first) / (1000 * 60 * 60 * 24));
}

let dateEnteredin, dateEnteredout;

document.getElementById("id_checkin").addEventListener("change", function () {
  let input = this.value;
  let dateEnteredin = new Date(input);
  console.log("Checkin date: " + dateEnteredin); //e.g. Fri Nov 13 2015 00:00:00 GMT+0000 (GMT Standard Time)
});

document.getElementById("id_checkout").addEventListener("change", function () {
  let input = this.value;
  let dateEnteredout = new Date(input);
  console.log("Checkout date: " + dateEnteredout); //e.g. Fri Nov 13 2015 00:00:00 GMT+0000 (GMT Standard Time)
});
