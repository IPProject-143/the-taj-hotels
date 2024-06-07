window.addEventListener("load", () => {
    document.querySelector(".preloader").classList.add("preloader-finish")
    document.querySelector(".others").classList.remove("boom")
    document.querySelector("body").classList.remove("overflow")

    setTimeout(() => {
        document.querySelector(".preloader").remove()
    }, 1000)
})