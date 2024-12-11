import streamlit as st

# 页面标题
st.title("和你女朋友的小互动")

# 问候语
st.write("亲爱的，今天怎么样呀？")

# 提问：今天你开心吗？
happy = st.radio("今天你开心吗？", ["是的", "有点不开心", "一般般"])

# 根据回答显示不同的消息
if happy == "是的":
    st.write("太好了，看到你开心我也很高兴！❤️")
elif happy == "有点不开心":
    st.write("不要担心，我会陪着你一起度过！💪")
else:
    st.write("每一天都充满了可能，慢慢来哦！😊")

st.divider()

# 提问：你今天想吃什么？
food = st.selectbox("今天你想吃什么？", ["火锅", "甜点", "外卖", "自己做", "其它"])

st.write(f"哦，今天我们可以一起吃{food}！🍴")

st.divider()

# 提问：你想去哪里玩？
destination = st.text_input("你想去哪玩？", "去海边")

if destination:
    st.write(f"好呀，去{destination}玩吧！🌴")

st.divider()

# 问她今天想做什么
activity = st.multiselect("你今天想做哪些事情？", 
                          ["看电影", "散步", "做运动", "一起做饭", "聊天", "炒菜"])

for act in activity:
    st.write(f"好主意，我们可以一起{act}！💖")

st.divider()

# 提供一些温馨的话语
st.write("亲爱的，感谢你总是陪伴我，不管生活怎样，你永远是我最宝贵的宝贝！💖")

# 上传一张你们的合照，作为互动的一部分
uploaded_file = st.file_uploader("上传你们的合照吧！", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="我们的美好回忆", use_column_width=True)

st.write("期待你上传的照片，和你一起回忆那些美好的时光！")
