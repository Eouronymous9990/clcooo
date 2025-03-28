# This is a sample Python script.
import streamlit as st


def main():
    st.title("آلة حاسبة بسيطة")

    num1 = st.number_input("أدخل الرقم الأول", value=0.0)
    num2 = st.number_input("أدخل الرقم الثاني", value=0.0)

    operation = st.selectbox("اختر العملية", ["جمع", "طرح", "ضرب", "قسمة"])

    result = None
    if operation == "جمع":
        result = num1 + num2
    elif operation == "طرح":
        result = num1 - num2
    elif operation == "ضرب":
        result = num1 * num2
    elif operation == "قسمة":
        result = num1 / num2 if num2 != 0 else "خطأ: القسمة على صفر!"

    if result is not None:
        st.success(f"النتيجة: {result}")


if __name__ == "__main__":
    main()
