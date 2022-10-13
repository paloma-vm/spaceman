// const itemList = document.getElementById('item-list')
// const cartQty = document.getElementById('cart-qty')
// const cartTotal = document.getElementById('cart-total')

// console.log(itemList)
// --------------------------------------------------------------
// I modified the mood-shop scripts so that I can 
// easily add more items to my page
import data from './data.js'
const itemsContainer = document.querySelector('#items')


for (let i = 0; i < data.length; i += 1) {
    const newDiv = document.createElement('div');
    newDiv.className = 'item'
    const img = document.createElement('img');

    img.src = data[i].image
    img.width = 320
    img.height = 213
    newDiv.appendChild(img)
    console.log(img)
    itemsContainer.appendChild(newDiv)

    const title = document.createElement('h2');
    title.innerText = data[i].title
    newDiv.appendChild(title)
    

    const desc = document.createElement('p');
    desc.innerText = data[i].desc
    newDiv.appendChild(desc)

    const date = document.createElement('p');
    date.innerText = data[i].date
    newDiv.appendChild(date)
    // console.log(date)
    


    const button = document.createElement('button');
    button.innerHTML = "Read More"
    newDiv.appendChild(button)

}