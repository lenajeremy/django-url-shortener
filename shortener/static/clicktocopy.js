const allRanges = []
const allClickables = document.querySelectorAll('table .btn-primary')

allClickables.forEach(clickable => {
  clickable.addEventListener('click', e => {
    let link = e.currentTarget.parentElement.parentElement.querySelector('input');
    link.select();
    document.execCommand('copy');
    e.currentTarget.innerHTML = 'Copied!!';
  })
})


document.querySelectorAll('.delete').forEach(button => {
  button.addEventListener('click', event => {
    const parent = event.currentTarget.parentElement.parentElement;
    console.log(parent.id, parent)
    fetch('/delete', {
      method: 'POST',
      body: JSON.stringify({ url_id: parent.id })
    }).then(data => data.json())
      .then(data => {
        if (data.done) {
          console.log(data)
          event.target.parentElement.parentElement.remove();
        } else {
          console.error(data)
        }
      })
      .catch(err => {
        console.error('An error occured')
        console.error(err)
      })
  })
})