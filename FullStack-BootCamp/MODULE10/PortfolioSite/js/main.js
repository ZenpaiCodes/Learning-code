const modalOpen = '[data-open]';
const modalClose = '[data-close]';
const isVisible = 'is-visible';

// document.querySelectorAll() Looks through the entire document, 
// then returns a NodeList
const openModal = document.querySelectorAll(modalOpen);
const closeModal = document.querySelectorAll(modalClose);

// Full Site Modal "open buttons"
for (const elm of openModal) {
  elm.addEventListener('click', function () {
    const modalId = this.dataset.open;
    document.getElementById(modalId).classList.add(isVisible);
  })
}

for (const elm of closeModal) {
  elm.addEventListener('click', function () {
    this.parentElement.parentElement.classList.remove(isVisible);
  })
}