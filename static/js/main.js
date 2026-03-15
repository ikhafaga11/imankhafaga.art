const backToTop = document.getElementById("backToTop")

window.addEventListener('scroll',() => {
    scrollY > 300 ? backToTop.style.display = "block" : backToTop.style.display = "none"
})

backToTop.addEventListener('click', () => {
window.scrollTo({
    top: 0,
    behavior: "smooth"
})
})

