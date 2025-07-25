import streamlit as st

# Simulated product listings for each platform
mock_products = {
    "BigBasket": [
        {"name": "Amul Milk 500ml", "brand": "Amul", "size": "500ml", "price": 26},
        {"name": "Amul Milk 1L", "brand": "Amul", "size": "1L", "price": 52},
    ],
    "Blinkit": [
        {"name": "Amul Milk 500ml", "brand": "Amul", "size": "500ml", "price": 25},
        {"name": "Amul Milk 1L", "brand": "Amul", "size": "1L", "price": 51},
    ],
    "Zepto": [
        {"name": "Amul Milk 500ml", "brand": "Amul", "size": "500ml", "price": 27},
        {"name": "Amul Milk 1L", "brand": "Amul", "size": "1L", "price": 53},
    ],
    "Amazon": [
        {"name": "Amul Milk 500ml", "brand": "Amul", "size": "500ml", "price": 28},
        {"name": "Amul Milk 1L", "brand": "Amul", "size": "1L", "price": 54},
    ],
    "DMart": [
        {"name": "Amul Milk 500ml", "brand": "Amul", "size": "500ml", "price": 24},
        {"name": "Amul Milk 1L", "brand": "Amul", "size": "1L", "price": 50},
    ],
}

# Initialize session state for cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🛒 Smart Grocery Cart Price Comparator")

# Input form for adding items
with st.form("add_item_form"):
    item_name = st.text_input("Item Name", value="milk")
    brand = st.text_input("Brand", value="Amul")
    size = st.text_input("Size/Weight", value="500ml")
    quantity = st.number_input("Quantity", min_value=1, value=1)
    submitted = st.form_submit_button("Add to Cart")
    if submitted:
        st.session_state.cart.append({
            "item_name": item_name.lower(),
            "brand": brand.lower(),
            "size": size.lower(),
            "quantity": quantity
        })
        st.success(f"Added {quantity} x {brand} {item_name} ({size}) to cart")

# Display current cart
st.subheader("🧾 Your Cart")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        st.write(f"{i+1}. {item['brand'].title()} {item['item_name'].title()} ({item['size']}) x {item['quantity']}")
else:
    st.info("Your cart is empty.")

# Price comparison
if st.session_state.cart:
    st.subheader("💰 Price Comparison")
    platform_totals = {}
    for platform, products in mock_products.items():
        total = 0
        for cart_item in st.session_state.cart:
            matched = next((p for p in products if p["name"].lower().startswith(f"{cart_item['brand']} {cart_item['item_name']}") and p["size"].lower() == cart_item["size"]), None)
            if matched:
                total += matched["price"] * cart_item["quantity"]
        platform_totals[platform] = total

    # Find the cheapest platform
    cheapest_platform = min(platform_totals, key=platform_totals.get)

    # Display results
    for platform, total in platform_totals.items():
        if platform == cheapest_platform:
            st.success(f"✅ {platform}: ₹{total}")
        else:
            st.write(f"{platform}: ₹{total}")

# Option to clear cart
if st.button("🗑️ Clear Cart"):
    st.session_state.cart = []
    st.experimental_rerun()
