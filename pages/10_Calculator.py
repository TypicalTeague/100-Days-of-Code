import streamlit as st
import art


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
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Page setup
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Calculator")

# Display your original logo
st.code(art.logo, language=None)


# Create session-state variables
if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "result" not in st.session_state:
    st.session_state.result = None

if "calculation_complete" not in st.session_state:
    st.session_state.calculation_complete = False

if "using_previous_result" not in st.session_state:
    st.session_state.using_previous_result = False

if "closed" not in st.session_state:
    st.session_state.closed = False


def reset_calculator():
    st.session_state.first_number = None
    st.session_state.result = None
    st.session_state.calculation_complete = False
    st.session_state.using_previous_result = False


def continue_with_result():
    st.session_state.first_number = st.session_state.result
    st.session_state.calculation_complete = False
    st.session_state.using_previous_result = True


def close_calculator():
    st.session_state.closed = True


# Closed screen
if st.session_state.closed:
    st.success("Calculator closed.")

    if st.button("Open Calculator Again"):
        reset_calculator()
        st.session_state.closed = False
        st.rerun()

    st.stop()


# Show the calculation form
if not st.session_state.calculation_complete:

    if st.session_state.using_previous_result:
        first_number = st.session_state.first_number
        st.info(f"Continuing with previous result: {first_number}")

    else:
        first_number = st.number_input(
            "Enter your first number:",
            value=None,
            placeholder="First number"
        )

    operator = st.radio(
        "Choose a mathematical operator:",
        options=list(operations.keys()),
        horizontal=True
    )

    second_number = st.number_input(
        "Enter your second number:",
        value=None,
        placeholder="Second number"
    )

    calculate = st.button(
        "Calculate",
        type="primary",
        use_container_width=True
    )

    if calculate:
        if first_number is None or second_number is None:
            st.error("Enter both numbers before calculating.")

        else:
            result = operations[operator](first_number, second_number)

            if result is None:
                st.error("Error: You cannot divide by zero.")

            else:
                st.session_state.first_number = first_number
                st.session_state.result = result
                st.session_state.operator = operator
                st.session_state.second_number = second_number
                st.session_state.calculation_complete = True
                st.rerun()


# Show the result and next choices
else:
    st.success(
        f"{st.session_state.first_number} "
        f"{st.session_state.operator} "
        f"{st.session_state.second_number} "
        f"= {st.session_state.result}"
    )

    st.write("What would you like to do next?")

    continue_column, new_column, quit_column = st.columns(3)

    with continue_column:
        if st.button(
            "Continue",
            help="Use this result as your next first number",
            use_container_width=True
        ):
            continue_with_result()
            st.rerun()

    with new_column:
        if st.button(
            "Start Over",
            help="Begin with a new first number",
            use_container_width=True
        ):
            reset_calculator()
            st.rerun()

    with quit_column:
        if st.button(
            "Quit",
            use_container_width=True
        ):
            close_calculator()
            st.rerun()