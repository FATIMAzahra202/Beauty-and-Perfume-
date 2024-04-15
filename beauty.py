import streamlit as st
import pandas as pd

# Initialize an empty DataFrame for beauty products
products_df = pd.DataFrame(columns=["Product ID", "Name", "Category", "Price", "In Stock"])

# Function to add products to the inventory
def add_product(df):
    st.subheader("Add a New Product")
    product_id = st.text_input("Product ID", key="product_id")
    name = st.text_input("Product Name", key="name")
    category = st.selectbox("Category", options=["Perfume", "Skincare", "Makeup", "Haircare"], key="category")
    price = st.number_input("Price ($)", key="price")
    in_stock = st.number_input("Units In Stock", min_value=0, key="in_stock")
    
    if st.button("Add Product"):
        new_data = {'Product ID': product_id, 'Name': name, 'Category': category, 'Price': price, 'In Stock': in_stock}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        st.success(f"Product {name} added successfully.")
    return df

# Function to display products
def display_products(df):
    st.subheader("Product Listings")
    st.dataframe(df)

# Customer Review Section
reviews_df = pd.DataFrame(columns=["Product ID", "Review", "Rating"])

def add_review(df):
    st.subheader("Add a Product Review")
    product_id = st.text_input("Product ID for Review", key="review_product_id")
    review = st.text_area("Review", key="review")
    rating = st.slider("Rating", 1, 5, key="rating")
    
    if st.button("Submit Review"):
        new_data = {'Product ID': product_id, 'Review': review, 'Rating': rating}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        st.success("Review submitted successfully.")
    return df

# Function to display reviews
def display_reviews(df):
    st.subheader("Customer Reviews")
    st.dataframe(df)

def main():
    global products_df, reviews_df
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose Option", ["Add Product", "View Products", "Add Review", "View Reviews"])
    
    if app_mode == "Add Product":
        products_df = add_product(products_df)
    elif app_mode == "View Products":
        display_products(products_df)
    elif app_mode == "Add Review":
        reviews_df = add_review(reviews_df)
    elif app_mode == "View Reviews":
        display_reviews(reviews_df)

if __name__ == "__main__":
    main()
