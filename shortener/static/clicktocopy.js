const allRanges = []
const allClickables = document.querySelectorAll('table .btn-primary')

allClickables.forEach(clickable => {
  clickable.addEventListener('click', e => {
    let link = e.currentTarget.parentElement.parentElement.querySelector('input');
    console.log(link);
    link.select();
    document.execCommand('copy', true);
    e.currentTarget.innerHTML = 'Copied!!';
  })
})
