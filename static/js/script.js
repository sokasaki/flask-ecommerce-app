// ============================================================================
// SHOPPING CART FUNCTIONALITY
// ============================================================================
// This file handles shopping cart operations for the e-commerce site.
// Product data is now fetched from the Flask backend API.
// ============================================================================

// ============================================================================
// CART STATE AND INITIALIZATION
// ============================================================================

let cart = []; // Initialize an empty cart array
const emptyCartMessage = document.getElementById("emptyCartMessage");
const totalElement = document.querySelector(".total h4");

// ============================================================================
// CART FUNCTIONS
// ============================================================================

// Add product to the cart
function addCartHome(selectedProduct) {
  if (selectedProduct) {
    const existingItem = cart.find(
      (item) => item.title === selectedProduct.title
    );
    if (existingItem) {
      existingItem.quantity = (existingItem.quantity || 1) + 1;
    } else {
      selectedProduct.quantity = 1;
      cart.push(selectedProduct);
    }
    displayCart();
  } else {
    console.error("Product not found or invalid product object passed.");
  }
}

// Display cart contents
function displayCart() {
  const offcanvasBody = document.querySelector(
    "#offcanvasCart .offcanvas-body"
  );
  if (!offcanvasBody) {
    console.error("Offcanvas body not found.");
    return;
  }

  if (cart.length === 0) {
    offcanvasBody.innerHTML =
      '<p class="text-muted text-center" id="emptyCartMessage">Your cart is empty.</p>';
    totalElement.innerHTML = "<h4>$0.00</h4>";
    document.querySelector(".icons.count").textContent = "0";
    return;
  }

  let cartHtml = "";
  let totalPrice = 0;
  let totalItems = 0;

  cart.forEach((item, index) => {
    const quantity = item.quantity || 1;
    const itemPrice = item.price * quantity;
    totalPrice += itemPrice;
    totalItems += quantity;
    cartHtml += `
            <div class="cart-item d-flex align-items-center mb-3 pb-3 border-bottom">
                <img src="${
                  item.image
                }.jpg" class="img-fluid rounded me-3" alt="${
      item.title
    }" style="width: 48px; height: 48px; object-fit: cover;">
                <div class="cart-item-details flex-grow-1">
                    <h6 class="cart-item-title mb-1">${item.title}</h6>
                    <div class="d-flex align-items-center mt-1">
                        <button class="btn btn-outline-secondary btn-sm px-2 me-1" type="button" onclick="changeQuantity(${index}, -1)"><i class="fa fa-minus"></i></button>
                        <span class="mx-2">${quantity}</span>
                        <button class="btn btn-outline-secondary btn-sm px-2 ms-1" type="button" onclick="changeQuantity(${index}, 1)"><i class="fa fa-plus"></i></button>
                    </div>
                </div>
                <div class="text-end ms-3">
                    <div class="fw-bold">$${itemPrice.toFixed(2)}</div>
                    <button type="button" class="btn btn-outline-danger btn-sm mt-2" aria-label="Remove" onclick="deleteItem(${index})"><i class="fa fa-trash"></i></button>
                </div>
            </div>
        `;
  });

  offcanvasBody.innerHTML = cartHtml;
  totalElement.innerHTML = `<h4>$${totalPrice.toFixed(2)}</h4>`;
  document.querySelector(".icons.count").textContent = totalItems.toString();
}

// Delete product from the cart
function deleteItem(index) {
  cart.splice(index, 1);
  displayCart();
}

// Add this function to handle quantity changes
function changeQuantity(index, delta) {
  if (cart[index]) {
    cart[index].quantity = Math.max(1, (cart[index].quantity || 1) + delta);
    displayCart();
  }
}

document.addEventListener("DOMContentLoaded", function () {
  // Navbar scroll effect
  const mainNavbar = document.getElementById("mainNavbar");
  if (mainNavbar) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 50) {
        // Adjust scroll threshold as needed
        mainNavbar.classList.add("scrolled");
      } else {
        mainNavbar.classList.remove("scrolled");
      }
    });
  }

  // Initialize display of featured products on homepage
  displayFeaturedProducts();

  // Display cart on load
  displayCart();
});
