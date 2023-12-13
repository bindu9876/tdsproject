import streamlit as st

def find_largest_num(n1,n2,n3):
    large=max(n1,n2,n3)
    return large

if __name__=="__main__":
    st.title("Finding the largest number amongst 3 given inputs")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest Number"):
        large = find_largest_num(num1, num2, num3)
        st.success(f"The largest number among {num1}, {num2}, and {num3} is {large}")