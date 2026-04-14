import streamlit as st

# ページの設定
st.set_page_config(page_title="干支チェッカー", page_icon="📅")

st.title("📅 動的・干支チェッカー")
st.write("西暦を入力すると、その年の情報を即座に表示します。")

# 入力欄（ここで数字を変えると動的に結果が変わります）
year = st.number_input("西暦を入力してください", min_value=0, max_value=3000, value=2026, step=1)

# 干支データの定義
junishi = [("子","ね"), ("丑","うし"), ("寅","とら"), ("卯","う"), ("辰","たつ"), ("巳","み"), 
           ("午","うま"), ("未","ひつじ"), ("申","さる"), ("酉","とり"), ("戌","いぬ"), ("亥","い")]
jikkan = [("庚","かのえ"), ("辛","かのと"), ("壬","みずのえ"), ("癸","みずのと"), ("甲","きのえ"), 
          ("乙","きのと"), ("丙","ひのえ"), ("丁","ひのと"), ("戊","つちのえ"), ("己","つちのと")]

# 計算（西暦を基準にしたインデックス算出）
k, k_y = jikkan[year % 10]
s, s_y = junishi[(year + 8) % 12]
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# 画面への表示
st.divider()
st.subheader(f"✨ {year}年はこんな年です")

col1, col2 = st.columns(2)
with col1:
    st.metric("正式な干支", f"{k}{s}")
    st.caption(f"読み：{k_y}{s_y}")

with col2:
    status = "閏年（366日）" if is_leap else "平年（365日）"
    st.metric("暦の区分", status)

st.info(f"一般的に親しまれている十二支（動物）は「{s_y}（{s}）」です。")