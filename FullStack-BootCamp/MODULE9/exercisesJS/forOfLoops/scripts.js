const header = document.querySelectorAll('h5');

for(const h of header){
  h.addEventListener('click', function() {
    console.log(this.textContent);
  });
}
