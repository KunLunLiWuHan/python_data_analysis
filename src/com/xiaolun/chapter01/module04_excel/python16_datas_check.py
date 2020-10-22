"""
@author:li kunlun
@time:2020-10-22
@description:数据校验-将无效成绩显示出来
"""
import pandas as pd


def score_valication(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}')


students = pd.read_excel('D:/Students.xlsx')
# axis=1表示跨列操作
students.apply(score_valication, axis=1)
