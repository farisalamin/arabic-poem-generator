const submitButton = document.querySelector('input[type="submit"]')
const form = submitButton.closest('form')
const poemContainer = document.querySelector('#poems')

form.addEventListener('submit', event => {
  event.preventDefault()
  submitButton.setAttribute('disabled', '')

  fetch(form.action, {
    method: form.method,
    body: new URLSearchParams(new FormData(form))
  })
  .then(response => response.json())
  .then(data => {
    submitButton.removeAttribute('disabled', '')
    poems.innerText = data['poem']
  })
})

const querySelector = selector => {}

querySelector('Hello World!')
