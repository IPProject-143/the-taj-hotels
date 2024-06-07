let input = document.getElementsByTagName("input");

for (let i = 0; i < input.length; i++) {
  const inpu = input[i];
  inpu.classList.add("input");
}

let hider = new IntersectionObserver((hider) => {
  hider.forEach((hideman) => {
    document
      .querySelector(".hider")
      .classList.add("show-hider", hideman.isIntersecting);
  });
});

const eror = document.querySelector(".errorlist");
hider.observe(eror);
