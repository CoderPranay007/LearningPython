import streamlit as st

def find_primes(start, end):
    primes = []
    for number in range(max(2, start), end + 1):
        if all(number % d != 0 for d in range(2, int(number**0.5) + 1)):
            primes.append(number)
    return primes

st.title("🔢 Prime Number Finder")

start = st.number_input("Start Number", min_value=0, value=2)
end = st.number_input("End Number", min_value=0, value=100)

if st.button("Find Primes"):
    if start > end:
        st.error("Start must be smaller than end.")
    else:
        primes = find_primes(int(start), int(end))
        if primes:
            st.success(f"Primes between {start} and {end}:")
            st.write(primes)
        else:
            st.warning("No primes found in that range.")
