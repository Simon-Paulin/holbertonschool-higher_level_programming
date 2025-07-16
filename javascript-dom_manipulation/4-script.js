document.querySelector('#add_item').addEventListener('click', function () {
  const new_list = document.createElement('li');
  new_list.textContent = 'Item';
  document.querySelector('.my_list').appendChild(new_list);
});