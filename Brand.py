import streamlit as st
from streamlit_option_menu import option_menu

# Set the title of the website and add a favicon
st.set_page_config(page_title="Clothing Brand", page_icon="👗")

# Initialize session state for basket
if 'basket' not in st.session_state:
    st.session_state.basket = []
if 'total_cost' not in st.session_state:
    st.session_state.total_cost = 0

# Function to add items to basket
def add_to_basket(item, price, size):
    st.session_state.basket.append(f"{item} - {size} - {price}$")
    st.session_state.total_cost += price
    st.success(f"Added {item} ({size}) to your basket.")

# Define the sidebar with icons
with st.sidebar:
    option = option_menu("Main Menu", ["Home", "About Us", "Products", "Basket", "Contact"], 
        icons=['house', 'info', 'shopping-cart', 'cart', 'envelope'], 
        menu_icon="cast", default_index=0)

# Home Page
if option == "Home":
    st.title("Welcome to Our Clothing Brand!")
    st.image("OIP.jpeg", width=300)
    st.write("""
        We offer the finest quality clothing tailored for you. 
        Explore our collection and find the perfect outfit that suits your style.
    """)

# About Us Page
elif option == "About Us":
    st.title("About Us")
    st.write("""
        We are a premium clothing brand dedicated to providing our customers with stylish, high-quality apparel. 
        Our mission is to create timeless pieces that are both comfortable and fashionable.
    """)

# Products Page
elif option == "Products":
    st.title("Our Products")
    col1, col2, col3 = st.columns(3)

    # Product 1: Bink outfit
    with col1:
        st.image("OIP (1).jpeg", caption="Bink outfit")
        st.write("Price: 2000$")
        size = st.selectbox("Select Size", ["S", "M", "L", "XL"], key="size_bink_outfit")
        if st.button("Add to Basket", key="Bink outfit"):
            add_to_basket("Bink outfit", 2000, size)

    # Product 2: Classic Collection
    with col2:
        st.image("recommend_0726_EU.jpg", caption="Classic Collection")
        st.write("Price: 500$")
        size = st.selectbox("Select Size", ["S", "M", "L", "XL"], key="size_classic_collection")
        if st.button("Add to Basket", key="Classic Collection"):
            add_to_basket("Classic Collection", 500, size)

    # Product 3: Brown Collection
    with col3:
        st.image("th.jpeg", caption="Brown Collection")
        st.write("Price: 1000$")
        size = st.selectbox("Select Size", ["S", "M", "L", "XL"], key="size_brown_collection")
        if st.button("Add to Basket", key="Brown Collection"):
            add_to_basket("Brown Collection", 1000, size)

# Basket Page
elif option == "Basket":
    st.title("Your Basket")
    if st.session_state.basket:
        for item in st.session_state.basket:
            st.write(f"- {item}")
        st.write(f"**Total Cost:** {st.session_state.total_cost}$")
    else:
        st.write("Your basket is empty.")
    
    if st.button("Clear Basket"):
        st.session_state.basket = []
        st.session_state.total_cost = 0
        st.success("Basket cleared!")

# Contact Page
elif option == "Contact":
    st.title("Contact Us")
    st.write("For inquiries, please reach us at:")
    st.write("📧 Email: tarekabdo1fg@gmail.com")
    st.write("📞 Phone: +201552115326")
    
    # Add a form for users to leave a message
    st.write("Feel free to leave us a message:")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Send Message"):
        st.success(f"Thank you, {name}! We will get back to you at {email} soon.")
