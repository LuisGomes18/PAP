function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Adicione manipuladores de eventos de clique aos links da barra de navegação
const links = document.querySelectorAll('#navbar a');
links.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Impede o comportamento padrão do link
        const sectionId = link.getAttribute('href').substring(1); // Remove o caractere '#' do href
        scrollToSection(sectionId);
    });
});