const allRanges = []
const allClickables = document.querySelectorAll('table .btn-primary')


allClickables.forEach(clickable => {
  let range = document.createRange(clickable);
  allRanges.push(range);
  clickable.addEventListener('click', e => {
    document.execCommand('copy', true);
    e.currentTarget.innerHTML = 'Copied!!';
  })
})
