// --- Filtering and Search Logic ---
// Only declare product array once at the top of the file

// let product = [
//     {
//         image: '../final_project/Men/hoody/Black/main',
//         title: 'hoodie',
//         price: 12.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: true // Added property for 'New' badge
//     },
//     {
//         image: '../final_project/Men/hoody/Brown/mainb',
//         title: 'HooDie',
//         price: 12.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/hoody/white/mainw',
//         title: 'Hoodie',
//         price: 12.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Shorts_With_Print/Beige/short-main',
//         title: 'Shorts With Print',
//         price: 10.00,
//         category: 'men',
//         subcategory: 'short',
//         isNew: true
//     },
//     {
//         image: '../final_project/Men/Shorts_With_Print/Black/short-main',
//         title: 'Shorts With Print',
//         price: 10.00,
//         category: 'men',
//         subcategory: 'short',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Shorts_With_Print/navy Blue/short-mainb',
//         title: 'Shorts With Print',
//         price: 10.00,
//         category: 'men',
//         subcategory: 'short',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Straight_Fit Shorts/Beige/ss-main',
//         title: 'Straight Fit Shorts',
//         price: 10.00,
//         category: 'men',
//         subcategory: 'short',
//         isNew: true
//     },
//     {
//         image: '../final_project/Men/Straight_Fit Shorts/Dark Green/Straight-Shorts-(main)',
//         title: 'Straight Fit Shorts',
//         price: 10.00,
//         category: 'men',
//         subcategory: 'short',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/T-Shirt/Black/T-Shirt (1main)',
//         title: 'T-Shirt',
//         price: 12.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/T-Shirt/Dark_Gray/T-Shirt (main)',
//         title: 'T-Shirt',
//         price: 12.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/T-Shirt/White/T-Shirtmain ',
//         title: 'T-Shirt',
//         price: 12.00,
//         category: 'men', // Added category for consistency
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/T-Shirt_With_Print/light Green/T-Shirt (5) (main)',
//         title: 'T-Shirt With Print',
//         price: 13.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/T-Shirt_With_Print/White/main',
//         title: 'T-Shirt With Print',
//         price: 13.00,
//         category: 'men',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Tank_Top_With_ Print/Beige/tt-main',
//         title: 'Tank Top With Print',
//         price: 9.00,
//         category: 'men',
//         subcategory: 't-shirt', // Changed to t-shirt as it's a top
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Tank_Top_With_ Print/Black/Tank-Topmain',
//         title: 'Tank Top With Print',
//         price: 9.00,
//         category: 'men',
//         subcategory: 't-shirt', // Changed to t-shirt as it's a top
//         isNew: false
//     },
//     {
//         image: '../final_project/Men/Tank_Top_With_ Print/Navy Blue/Tank-Top main',
//         title: 'Tank Top With Print',
//         price: 9.00,
//         category: 'men',
//         subcategory: 't-shirt', // Changed to t-shirt as it's a top
//         isNew: false
//     },
//     // lady
//     {
//         image: '../final_project/Lady/Cami Mini Dress/Light Blue/Mini-Dress (main)',
//         title: 'Cami Mini Dress',
//         price: 29.00,
//         category: 'lady',
//         subcategory: 'dress',
//         isSale: true // Added property for 'Sale' badge
//     },
//     {
//         image: '../final_project/Lady/Cami Mini Dress/white/Mini-Dress (main)',
//         title: 'Cami Mini Dress',
//         price: 29.00,
//         category: 'lady',
//         subcategory: 'dress',
//         isSale: false
//     },
//     {
//         image: '../final_project/Lady/Crop Sweat Jacket/Black/Jacket (main)',
//         title: 'Crop Sweat Jacket',
//         price: 14.00,
//         category: 'lady',
//         subcategory: 'sweatpant',
//         isNew: true
//     },
//     {
//         image: '../final_project/Lady/Crop Sweat Jacket/White/Jacket (main)',
//         title: 'Crop Sweat Jacket',
//         price: 14.00,
//         category: 'lady',
//         subcategory: 'sweatpant',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Cropped T-shirt With Print/Blue Wash/Cropped-T-Shirt-With-Print (main)',
//         title: 'Cropped T-shirt With Print',
//         price: 16.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Cropped T-shirt With Print/Olive Green/Cropped-T-Shirt-With-Print (main)',
//         title: 'Cropped T-shirt With Print',
//         price: 16.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Cropped T-Shirt With Print1/navy/T-Shirt (main)',
//         title: 'Cropped T-shirt With Print',
//         price: 16.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Cropped T-Shirt With Print1/Red/T-Shirt (main)',
//         title: 'Cropped T-shirt With Print',
//         price: 16.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Midi Dress/Black/Mini-Dress (main)',
//         title: 'Midi Dress',
//         price: 25.00,
//         category: 'lady',
//         subcategory: 'dress',
//         isSale: true
//     },
//     {
//         image: '../final_project/Lady/Midi Dress/Pink/Mini-Dress (main)',
//         title: 'Midi Dress',
//         price: 25.00,
//         category: 'lady',
//         subcategory: 'dress',
//         isSale: false
//     },
//     {
//         image: '../final_project/Lady/Off Shoulder T-Shirt/Black/T-Shirt (main)',
//         title: 'Off Shoulder T-Shirt',
//         price: 17.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Off Shoulder T-Shirt/White/T-Shirt (main)',
//         title: 'Off Shoulder T-Shirt',
//         price: 17.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/T-Shirt With Print/Light Pink/T-Shirt (main)-1',
//         title: 'T-Shirt With Print',
//         price: 10.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/T-Shirt With Print/White/T-Shirt (main)',
//         title: 'T-Shirt With Print',
//         price: 10.00,
//         category: 'lady',
//         subcategory: 't-shirt',
//         isNew: false
//     },
//     {
//         image: '../final_project/Lady/Wide Leg Sweatpants/Black/Trouser (main)',
//         title: 'Wide Leg Sweatpants',
//         price: 15.00,
//         category: 'lady',
//         subcategory: 'sweatpant',
//         isSale: true
//     },
//     {
//         image: '../final_project/Lady/Wide Leg Sweatpants/White/Trouser (main)',
//         title: 'Wide Leg Sweatpants',
//         price: 15.00,
//         category: 'lady',
//         subcategory: 'sweatpant',
//         isSale: false
//     },
// ];

// Now filteredProducts will have all products
// let filteredProducts = [...product];

function applyFiltersAndSearch() {
    // Get filter values
    const category = document.getElementById('categoryFilter')?.value || 'all';
    const subcategory = document.getElementById('subcategoryFilter')?.value || 'all';
    const search = document.getElementById('searchInput')?.value.trim().toLowerCase() || '';

    filteredProducts = product.filter(item => {
        let match = true;
        if (category !== 'all') {
            match = match && item.category === category;
        }
        if (subcategory !== 'all') {
            match = match && item.subcategory === subcategory;
        }
        if (search) {
            match = match && item.title.toLowerCase().includes(search);
        }
        return match;
    });
    showingAllProducts = false;
    displayAllProducts();
}

// Listen for filter form submit
document.getElementById('filterForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    applyFiltersAndSearch();
});

// Listen for search form submit
document.getElementById('searchForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    applyFiltersAndSearch();
});

// Listen for sort select
document.getElementById('sortSelect')?.addEventListener('change', function(e) {
    const value = e.target.value;
    if (value === 'price-asc') {
        filteredProducts.sort((a, b) => a.price - b.price);
    } else if (value === 'price-desc') {
        filteredProducts.sort((a, b) => b.price - a.price);
    } else if (value === 'name-asc') {
        filteredProducts.sort((a, b) => a.title.localeCompare(b.title));
    } else if (value === 'name-desc') {
        filteredProducts.sort((a, b) => b.title.localeCompare(a.title));
    } else {
        filteredProducts = [...filteredProducts]; // No sort
    }
    showingAllProducts = false;
    displayAllProducts();
});

let cart = []; // Initialize an empty cart array
const con = document.querySelector('.con'); // For featured products on index.html
const shopCon = document.querySelector('.shop-con'); // For all products on shop.html
const showMoreContainer = document.getElementById('showMoreContainer'); // For the Show More button
const emptyCartMessage = document.getElementById('emptyCartMessage');
const totalElement = document.querySelector('.total h4');

// Display products for the "Latest Arrivals" section on index.html
function displayFeaturedProducts() {
    let setPro = '';
    // Take a subset of products, e.g., the first 8, or products marked as new
    const featured = product.filter(item => item.isNew).slice(0, 8); // Display up to 8 new products

    if (featured.length === 0) {
        con.innerHTML = '<p class="text-center text-muted col-12 my-5 fs-4">No new products to display.</p>';
        return;
    }

    featured.forEach((productItem) => {
        let badgeHtml = '';
        if (productItem.isNew) {
            badgeHtml = '<div class="product-badge new-badge">NEW</div>';
        } else if (productItem.isSale) {
            badgeHtml = '<div class="product-badge sale-badge">SALE</div>';
        }

        setPro += `
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-4 product-card">
                <div class="card">
                    ${badgeHtml}
                    <img src="${productItem.image}.jpg" class="card-img-top" alt="${productItem.title}" loading="lazy">
                    <div class="card-body text-center">
                        <h5 class="card-title fw-semibold text-truncate mb-1">${productItem.title}</h5>
                        <p class="card-text text-muted small mb-2">${productItem.category.charAt(0).toUpperCase() + productItem.category.slice(1)}</p>
                        <p class="card-text fw-bold fs-5 text-dark product-price">$${productItem.price.toFixed(2)}</p>
                        <button type="button" class="btn btn-primary add-to-cart-btn mt-auto" onclick="addCartHome(${JSON.stringify(productItem).replace(/\"/g, '&quot;')})">Add to cart</button>
                    </div>
                </div>
            </div>
        `;
    });

    con.innerHTML = setPro;
}

// Display all products for the shop page
let showingAllProducts = false;

function displayAllProducts() {
    if (!shopCon) return;
    let allPro = '';
    const initialCount = 8; // Number of products to show initially
    let productsToShow = showingAllProducts ? filteredProducts : filteredProducts.slice(0, initialCount);

    if (filteredProducts.length === 0) {
        shopCon.innerHTML = '<p class="text-center text-muted col-12 my-5 fs-4">No products to display.</p>';
        if (showMoreContainer) showMoreContainer.innerHTML = '';
        return;
    }

    productsToShow.forEach((productItem) => {
        let badgeHtml = '';
        if (productItem.isNew) {
            badgeHtml = '<div class="product-badge new-badge">NEW</div>';
        } else if (productItem.isSale) {
            badgeHtml = '<div class="product-badge sale-badge">SALE</div>';
        }
        allPro += `
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-4 product-card">
                <div class="card">
                    ${badgeHtml}
                    <img src="${productItem.image}.jpg" class="card-img-top" alt="${productItem.title}" loading="lazy">
                    <div class="card-body text-center">
                        <h5 class="card-title fw-semibold text-truncate mb-1">${productItem.title}</h5>
                        <p class="card-text text-muted small mb-2">${productItem.category.charAt(0).toUpperCase() + productItem.category.slice(1)}</p>
                        <p class="card-text fw-bold fs-5 text-dark product-price">$${productItem.price.toFixed(2)}</p>
                        <button type="button" class="btn btn-primary add-to-cart-btn mt-auto" onclick="addCartHome(${JSON.stringify(productItem).replace(/\"/g, '&quot;')})">Add to cart</button>
                    </div>
                </div>
            </div>
        `;
    });
    shopCon.innerHTML = allPro;

    // Show More button logic
    if (!showingAllProducts && filteredProducts.length > initialCount) {
        if (showMoreContainer) {
            showMoreContainer.innerHTML = '<button id="showMoreBtn" class="btn btn-outline-primary">Show More</button>';
            document.getElementById('showMoreBtn').onclick = function() {
                showingAllProducts = true;
                displayAllProducts();
            };
        }
    } else if (showMoreContainer) {
        showMoreContainer.innerHTML = '';
    }
}

// Add product to the cart (from homepage featured products)
function addCartHome(selectedProduct) {
    if (selectedProduct) {
        const existingItem = cart.find(item => item.title === selectedProduct.title);
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
    const offcanvasBody = document.querySelector('#offcanvasCart .offcanvas-body');
    if (!offcanvasBody) {
        console.error("Offcanvas body not found.");
        return;
    }

    if (cart.length === 0) {
        offcanvasBody.innerHTML = '<p class="text-muted text-center" id="emptyCartMessage">Your cart is empty.</p>';
        totalElement.innerHTML = '<h4>$0.00</h4>';
        document.querySelector('.icons.count').textContent = '0';
        return;
    }

    let cartHtml = '';
    let totalPrice = 0;
    let totalItems = 0;

    cart.forEach((item, index) => {
        const itemPrice = item.price * (item.quantity || 1);
        totalPrice += itemPrice;
        totalItems += (item.quantity || 1);
        cartHtml += `
            <div class="cart-item d-flex align-items-center mb-3 pb-3 border-bottom">
                <img src="${item.image}.jpg" class="img-fluid rounded me-3" alt="${item.title}" style="width: 70px; height: 70px; object-fit: cover;">
                <div class="cart-item-details flex-grow-1">
                    <h6 class="cart-item-title mb-1">${item.title}</h6>
                    <p class="cart-item-price mb-0 text-muted">$${item.price.toFixed(2)} x ${item.quantity || 1}</p>
                </div>
                <button type="button" class="btn-close ms-auto cart-item-remove" aria-label="Remove" onclick="deleteItem(${index})"></button>
            </div>
        `;
    });

    offcanvasBody.innerHTML = cartHtml;
    totalElement.innerHTML = `<h4>$${totalPrice.toFixed(2)}</h4>`;
    document.querySelector('.icons.count').textContent = totalItems.toString();
}

// Delete product from the cart
function deleteItem(index) {
    cart.splice(index, 1);
    displayCart();
}

document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const mainNavbar = document.getElementById('mainNavbar');
    if (mainNavbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) { // Adjust scroll threshold as needed
                mainNavbar.classList.add('scrolled');
            } else {
                mainNavbar.classList.remove('scrolled');
            }
        });
    }

    // Initialize display of featured products on homepage
    if (con) displayFeaturedProducts();

    // Initialize display of all products on shop page
    if (shopCon) {
        filteredProducts = [...product];
        displayAllProducts();
    }

    // Display cart on load
    displayCart();
});