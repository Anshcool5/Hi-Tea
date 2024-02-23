const scriptURL = 'https://script.google.com/macros/s/AKfycbyhJUXovuWn8Zec6FqwmAxZZuStwU5PoQT0v0tmbYhbI14FjHr1aVce45tS0lH58XdBbw/exec'

const form = document.forms['myForm']

form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
  .then(response => alert("Thank you! your form is submitted successfully." ))
  .then(() => { window.location.reload(); })
  .catch(error => console.error('Error!', error.message))
})

