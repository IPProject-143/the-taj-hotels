// Login button starts here

document.querySelector(".login").addEventListener("click", () => {
  window.open("/register", "_self");
});

// Login button ends here

// Why section starts here

const splide = new Splide(".splide", {
  paginationKeyboard: true,
  type: "loop",
  drag: true,
}).mount();

// Why section ends here

// Hotel previews start here

document.querySelector(".load-more").addEventListener("click", () => {
  window.open("/hotels", "_self");
});

// Hotel previews end here

// User testimonials start here

const swiper = new Swiper(".js-testimonials-slider", {
  grabCursor: true,
  spaceBetween: 30,
  pagination: {
    el: ".js-testimonials-pagination",
    clickable: true,
  },
  slidesPerView: 2,
});

// User testimonials end here

// Help section starts here

document.querySelector(".fa-instagram").addEventListener("click", () => {
  window.open("https://www.instagram.com");
});

document.querySelector(".fa-x-twitter").addEventListener("click", () => {
  window.open("https://www.x.com");
});
document.querySelector(".fa-facebook").addEventListener("click", () => {
  window.open("https://www.facebook.com");
});

// Help section ends here
