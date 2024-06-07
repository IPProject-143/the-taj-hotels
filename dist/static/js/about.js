let text = document.querySelector(".text");
let img1 = document.querySelector(".img1");
let img2 = document.querySelector(".img2");
let img3 = document.querySelector(".img3");

window.addEventListener("scroll", () => {
  // Logic for parallax starts here

  let y = window.scrollY;
  text.style.marginTop = y * -2 + "px";
  img1.style.marginTop = y * 0.75 + "px";
  img2.style.marginTop = y * 0.5 + "px";
  img3.style.marginTop = y * 0.25 + "px";

  // Logic for parallax ends here

  // Logic for navbar starts here
  let header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 569);

  if (window.scrollY >= 569) {
    header
      .querySelector("svg")
      .querySelector("path")
      .setAttribute("fill", "black");
  } else {
    header
      .querySelector("svg")
      .querySelector("path")
      .setAttribute("fill", "white");
  }

  // Logic for navbar ends here
});
