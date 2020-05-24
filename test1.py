# จัดลำดับของ player ตาม score และใส่ rank ให้ตามลำดับเรียงจาก score มากสุด

player = [
    {'Name':'A', 'score': 50},
    {'Name':'B', 'score': 60},
    {'Name':'C', 'score': 85},
    {'Name':'D', 'score': 80},
    {'Name':'E', 'score': 90}
]

rank = ['Gold', 'Silver', 'Bronze']

# ผลลัพธ์
# [
#     {'Name': 'E', 'score': 90, 'rank': 'Gold'}, 
#     {'Name': 'C', 'score': 85, 'rank': 'Silver'}, 
#     {'Name': 'D', 'score': 80, 'rank': 'Bronze'}, 
#     {'Name': 'B', 'score': 60, 'rank': '-'}, 
#     {'Name': 'A', 'score': 50, 'rank': '-'}
# ]
