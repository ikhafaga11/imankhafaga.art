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

const input = document.getElementById("file-input");
const preview = document.getElementById("preview")

input.addEventListener("change", () => {
    const file = input.files[0];

    if(file) {
        const url = URL.createObjectURL(file);
        preview.src = url;
        preview.style.display = "block";
    }
})