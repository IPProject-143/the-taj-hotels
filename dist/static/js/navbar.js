window.addEventListener("scroll", () => {
    let header = document.querySelector("header")
    header.classList.toggle("sticky", window.scrollY > 0)
    
    if (window.scrollY > 0) {
        header.querySelector("svg").querySelector("path").setAttribute("fill", "black")
    } else {
        header.querySelector("svg").querySelector("path").setAttribute("fill", "white")
    }

})

