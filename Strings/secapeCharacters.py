# txt = "저는 "개발자" 가 아닙니다."
# 이거 안됨. ""안에 또 ""가 들어가면 에러남.

txt = "저는 \"개발자\" 가 아닙니다."
print(txt)
#그래서 escape문자를 넣음. "앞에 \를 넣거나 \\를 넣거나 \n으로 강제개행을 하던가 하면 됨.