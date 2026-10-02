import streamlit as st

# --- Your Original Classes ---
class Bankcacount:
    def __init__(self, name, balance):
        self.name = name    
        
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            st.error("Balance can't be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            st.success(f"Amount deposited: {amount}")
        else:
            st.error("Invalid deposit amount")

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            st.success(f"Amount withdrawn: {amount}")
        else:
            st.error("Insufficient balance or invalid amount")

    def display(self):
        st.write(f"**Name:** {self.name}")
        st.write(f"**Balance:** {self.balance}")


class Savings_account(Bankcacount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def show_detais(self):
        st.write(f"**Name:** {self.name}")
        st.write(f"**Balance:** {self.balance}")
        st.write(f"**Interest Rate:** {self.interest_rate}%")


class Fixed_deposit(Bankcacount):
    def __init__(self, name, balance, maturity_date):
        super().__init__(name, balance)
        self.maturity_date = maturity_date

    def show_fd_details(self):
        self.display()
        st.write(f"**Maturity Date:** {self.maturity_date}")


# --- Streamlit UI App ---
st.title("🏦 Bank Account Management System")

# Initialize Session State objects so data persists between button clicks
if "savings_acc" not in st.session_state:
    st.session_state.savings_acc = Savings_account("Mansi", 2000, 4)

if "fd_acc" not in st.session_state:
    st.session_state.fd_acc = Fixed_deposit("Mansi", 10000, "12 months")

# Sidebar navigation
option = st.sidebar.selectbox("Choose Account Type", ["Savings Account", "Fixed Deposit Account"])

if option == "Savings Account":
    st.header("Savings Account Dashboard")
    
    # Display Details
    if st.button("Show Account Details"):
        st.session_state.savings_acc.show_detais()

    st.divider()

    # Deposit Section
    st.subheader("Deposit Money")
    dep_amount = st.number_input("Deposit Amount", min_value=0.0, step=100.0, key="dep_input")
    if st.button("Deposit"):
        st.session_state.savings_acc.deposit(dep_amount)

    # Withdrawal Section
    st.subheader("Withdraw Money")
    wit_amount = st.number_input("Withdrawal Amount", min_value=0.0, step=100.0, key="wit_input")
    if st.button("Withdraw"):
        st.session_state.savings_acc.withdrawal(wit_amount)

    # Display Updated Balance
    st.info(f"Current Balance: {st.session_state.savings_acc.balance}")

elif option == "Fixed Deposit Account":
    st.header("Fixed Deposit Dashboard")
    
    if st.button("Show FD Details"):
        st.session_state.fd_acc.show_fd_details()