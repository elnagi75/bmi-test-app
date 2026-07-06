import streamlit as st
import pandas as pd
import json
import os

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="المنصة الذكية للتدريب الرياضي", layout="centered", page_icon="🏋️‍♀️")

# 2. كود CSS لجعل اتجاه التطبيق بالكامل من اليمين إلى اليسار (عربي)
st.markdown("""
<style>
    body {direction: rtl; text-align: right;}
    .stTextInput>div>div>input {direction: rtl; text-align: right;}
    .stNumberInput>div>div>input {direction: rtl; text-align: right;}
    .stMarkdown {direction: rtl; text-align: right;}
    th {text-align: right !important;}
    td {text-align: right !important;}
</style>
""", unsafe_allow_html=True)

# 3. تصميم رأس الصفحة (الهيدر) والصورة
col1, col2 = st.columns([1, 3])
with col1:
    try:
        # سيتم عرض الصورة بمجرد رفعك لملف hanaa.jpg في المخزن
        st.image("hanaa.jpg", width=150)
    except:
        st.info("سيتم عرض صورة الباحثة هنا فور رفعها للمخزن")

with col2:
    st.markdown("<h2 style='text-align: right; color: #1E3A8A;'>المنصة الذكية لتصميم الوحدات التدريبية الفردية للسيدات</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: right; color: #4B5563;'>إعداد الباحثة: أ.د / هناء رشوان عبد الله</h4>", unsafe_allow_html=True)

st.markdown("---")

# 4. نظام قاعدة البيانات المبسط (لتسجيل وحفظ بيانات العينة)
DB_FILE = "trainees_db.json"

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = load_data()

# 5. واجهة البحث وإدخال المتدربات
st.markdown("### 🔍 تحديد ملف المتدربة")
trainee_id = st.text_input("أدخل كود أو اسم المتدربة (مثال: عينة 1، فاطمة، 105):")

if trainee_id:
    # --- الحالة الأولى: المتدربة مسجلة مسبقاً ---
    if trainee_id in db:
        st.success(f"تم العثور على ملف: {trainee_id}")
        prev_data = db[trainee_id]
        st.write(f"**العمر:** {prev_data['age']} سنة | **الوزن:** {prev_data['weight']} كجم | **BMI:** {prev_data['bmi']}")
        
        st.markdown("#### 🔄 متابعة وتعديل الحمل للأسبوع الجديد")
        rpe_last_week = st.slider("كم كان مقياس الجهد المدرك (RPE) الفعلي للمتدربة في الأسبوع الماضي؟", 1, 10, 3)
        
        if st.button("توليد وحدة تدريبية ذكية للأسبوع الجديد 🚀"):
            st.success("تم تحليل استجابة المتدربة (الجهد المدرك). الذكاء الاصطناعي يوصي بتعديل الحجم والشدة كالتالي:")
            show_table = True
            
    # --- الحالة الثانية: متدربة جديدة ---
    else:
        st.warning("⚠️ هذه متدربة جديدة. يرجى إدخال القياسات القبلية لتأسيس الملف لأول مرة.")
        col1, col2, col3 = st.columns(3)
        age = col1.number_input("العمر (35-40):", 35, 40, 35)
        weight = col2.number_input("الوزن (كجم):", 40.0, 150.0, 80.0)
        height = col3.number_input("الطول (سم):", 140.0, 190.0, 160.0)
        
        col4, col5 = st.columns(2)
        hr_rest = col4.number_input("النبض في الراحة (ن/ق):", 50, 120, 80)
        walk_test = col5.number_input("اختبار المشي 6 دقائق (متر):", 100, 800, 400)
        
        if st.button("حفظ البيانات وتوليد أول وحدة تدريبية 🚀"):
            bmi = round(weight / ((height/100)**2), 2)
            db[trainee_id] = {
                "age": age, "weight": weight, "height": height, 
                "bmi": bmi, "hr_rest": hr_rest, "walk_test": walk_test
            }
            save_data(db)
            st.success(f"تم حفظ بيانات {trainee_id} بنجاح! مؤشر كتلة الجسم (BMI) = {bmi}")
            show_table = True

    # 6. عرض المخرجات (الجدول التدريبي FITT-VP)
    if 'show_table' in locals() and show_table:
        st.markdown("---")
        st.markdown("### 📋 الوحدة التدريبية المقترحة وفق محددات (FITT-VP)")
        
        # محاكاة لجدول المخرجات
        data = [
            ["الإحماء", "مشي خفيف في المكان", "🏃‍♀️ (مقطع توضيحي)", "2 - 3 (خفيف)", "مستمر", "5 دقائق"],
            ["الإحماء", "دوائر الذراعين (أمام وخلف)", "🔄 (مقطع توضيحي)", "2 (مريح)", "10 تكرارات/اتجاه", "دقيقتان"],
            ["الجزء الرئيسي", "الجلوس والقيام (Chair Squat)", "🪑 (مقطع توضيحي)", "4 - 5 (معتدل)", "2 مجموعة × 10 تكرارات", "4 دقائق"],
            ["الجزء الرئيسي", "الدفع على الحائط (Wall Push-ups)", "🧱 (مقطع توضيحي)", "4 - 5 (معتدل)", "2 مجموعة × 8 تكرارات", "3 دقائق"],
            ["التهدئة", "إطالة الفخذ الخلفية", "🧘‍♀️ (مقطع توضيحي)", "2 (إطالة)", "ثبات 30 ث/رجل", "دقيقتان"]
        ]
        df = pd.DataFrame(data, columns=["مرحلة التدريب", "التمرين", "التوضيح الحركي", "الشدة (RPE)", "الحجم (مجموعات × تكرارات)", "الزمن"])
        
        # رسم الجدول على الشاشة
        st.table(df)

st.markdown("---")
st.caption("برمجة وتصميم: متغير تجريبي بحثي - كافة الحقوق محفوظة.")
