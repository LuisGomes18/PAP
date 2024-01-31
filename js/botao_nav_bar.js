function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId)
    if (section) {
        section.scrollIntoView({ behavior: "smooth" })
    }
}

const links = document.querySelectorAll("#navbar a")
links.forEach((link) => {
    link.addEventListener("click", (event) => {
        event.preventDefault()
        const sectionId = link.getAttribute("href").substring(1)
        scrollToSection(sectionId)
    })
})
