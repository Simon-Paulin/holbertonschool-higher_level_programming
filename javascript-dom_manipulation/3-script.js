document.querySelector('#toggle_header').addEventListener('click', function () {
  const heading = document.querySelector('header');
  if (heading.classList.contains('red')) {
    heading.classList.replace('red', 'green');
  } else {
    heading.classList.replace('green', 'red');
  }
});