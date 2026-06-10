import streamlit as st

# Define mathematical operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# App UI configuration
st.title("🧮 Interactive Calculator")

# Initialize session state to track the previous calculation result
if 'previous_result' not in st.session_state:
    st.session_state.previous_result = None

# Let the user use the previous result if it exists
use_previous = False
if st.session_state.previous_result is not None:
    use_previous = st.checkbox(f"Continue with previous result? ({st.session_state.previous_result})")

# Input fields based on whether previous result is used
if use_previous:
    num1 = st.session_state.previous_result
    st.info(f"First number fixed to: {num1}")
else:
    num1 = st.number_input("Enter your first number:", value=0.0, step=1.0)

# Operator and second number selection
operator = st.selectbox("Select an operator:", options=list(operations.keys()))
num2 = st.number_input("Enter your second number:", value=0.0, step=1.0)

# Calculate button
if st.button("Calculate", type="primary"):
    if operator == '/' and num2 == 0:
        st.error("Error: Division by zero is not allowed.")
    else:
        result = operations[operator](num1, num2)
        if result is not None:
            st.success(f"Result: {num1} {operator} {num2} = **{result}**")
            # Update session state with the new result
            st.session_state.previous_result = result

# Reset / Clear button to clear previous result memory
if st.button("Clear Memory"):
    st.session_state.previous_result = None
    st.rerun()