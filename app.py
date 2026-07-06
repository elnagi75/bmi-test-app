import streamlit as st

# إعدادات واجهة التطبيق
st.set_page_config(page_title="تطبيق حساب مؤشر كتلة الجسم", page_icon="⚖️")

st.title("تطبيق حساب مؤشر كتلة الجسم (BMI) - نسخة تجريبية")
st.write("أهلاً بك يا دكتور في أول تطبيق ويب لك! أدخل البيانات أدناه للتجربة:")

# خانات الإدخال
weight = st.number_input("الوزن (بالكيلوجرام):", min_value=30.0, max_value=200.0, value=70.0, step=1.0)
height_cm = st.number_input("الطول (بالسنتيمتر):", min_value=100.0, max_value=250.0, value=170.0, step=1.0)

# زر الحساب
if st.button("احسب BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    
    st.success(f"مؤشر كتلة الجسم (BMI) هو: {bmi:.2f}")
    
    # تحديد الفئة
    if bmi < 18.5:
        st.warning("تصنيف الحالة: نقص في الوزن")
    elif 18.5 <= bmi < 24.9:
        st.info("تصنيف الحالة: وزن طبيعي ومثالي")
    elif 25 <= bmi < 29.9:
        st.warning("تصنيف الحالة: زيادة في الوزن")
    else:
        st.error("تصنيف الحالة: سمنة")
        
st.markdown("---")
st.caption("تم تصميم هذا التطبيق التجريبي لاختبار بيئة عمل Streamlit لمشروع البحث الأكاديمي.")
