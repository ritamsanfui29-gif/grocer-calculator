# Exercise Title: The Smart Grocer Calculator

# Scenario:
# A grocery store sells three items:
# - Rice – ₹60 per kg
# - Sugar – ₹45 per kg
# - Oil – ₹120 per litre
# The customer enters the quantity of each item they wish to buy.
# If the total cost exceeds ₹500, they get a 10% discount.
# Your Task:
# 1. Ask the user to input the quantities of each item.
# 2. Calculate the total cost based on prices.
# 3. If the total is above ₹500, apply a 10% discount.
# 4. Display the total before discount, discount applied, and final amount to pay

import streamlit as st

st.title(" 🛒 The Smart Grocer Calculator")
name = st.text_input("Enter your name: ")
if name :
    st.success(f"CUSTOMAR NAME: {name}")

st.header("⚖️ QYANTITIES")
st.subheader("(enter your quantities)")

rice_price = 60,   # per kg
suger_price = 45,  # per kg
oil_price = 120   # per litre

rice_qty = st.number_input("Rice (kg)", min_value = 0.0, step = 0.5)
suger_qty = st.number_input("Suger (kg)", min_value = 0.0, step = 0.5)
oil_qty = st.number_input("oil (litre)", min_value = 0.0, step = 0.5)

total = (rice_qty * 60) + (suger_qty * 45) + (oil_qty * 120)


if st.button("CALCUTALE"):
    st.subheader("🧾 YOUR Bill:")
    if total > 500 :
        discount = total * 0.10
        final_discount = total - discount
        st.success(f"🎉 You got the 10% discount of RS.{discount:.2f}")
    else :
        final_discount = total
        st.write(f"SORRY You just missed the discount")
        st.success(f"YOUR TOTAL AMOUNT IS RS. {total}")
    if total > 500 :
        discount = total * 0.10
        final_discount = total - discount
        st.success("🎊 DISCOUNT APPLIED 🎊")
        st.success(f" FINAL AMOUNT: RS.{final_discount}")
    else:
        st.write("DICOUNT NOT APPLIDED")
        st.success(f" FINAL AMOUNT: RS.{final_discount}")
