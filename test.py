#위/아래로 붙이기 
# 이번에는 데이터프레임을 위/아래로 이어 붙여 보겠습니다. 
# 두 개의 데이터프레임의 컬럼을 기준으로 정렬한 후 위/아래로 붙여서 
# 새로운 데이터프레임을 생성할 수 있습니다. 
from pandas import DataFrame
import pandas as pd

# 첫 번째 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data, index=index)

# 두 번째 데이터프레임
data = {
    '종가': [110000, 483689],
    '거래량': [109000, 791946]
}
index = ["2019-06-19", "2019-06-18"]
df2 = DataFrame(data, index=index)

print( df1 )
print( df2 )

print("---위아래 붙이기---")
df = df1.append(df2)
df