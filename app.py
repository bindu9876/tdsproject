import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # User input
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Find the largest number
    result = find_largest(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
