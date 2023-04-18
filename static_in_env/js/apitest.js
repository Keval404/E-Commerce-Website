let productContainer = document.getElementById('apitesting')
let getProducts = async () => {
  let response = await fetch('http://127.0.0.1:8000/api/item/')
  let products = await response.json();
  console.log(products)
  let initial = `<h3 id="productHead">Our<span> Products</span></h3>`
  productContainer.innerHTML += initial;
  for (let i = 0; i < products.length; i++) {
    let product = products[i]
    console.log(product)
    let row = `<div class="prod-slider swiper mySwiper">
                <div class="wrapper swiper-wrapper">
                  ${product.id}
                  <div
                    class="prods swiper-slide"
                    style="background-image: url('${product.image}');"
                    id="p1"
                  >
                    <h3>${product.title}</h3>
                    <p>From Rs.${product.price}/-</p>
                    <button class="learnmore">
                      <a href="{{item.get_absolute_url}}">Buy Now</a>
                    </button>
                  </div>
                </div>
              </div>`

    productContainer.innerHTML += row
  } 
}
getProducts()
