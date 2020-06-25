# สร้าง function ด้วยภาษาที่ถนัดจัดลำดับของ player ตาม score และใส่ rank ให้ตามลำดับเรียงจาก score มากสุด

player = [
    {'Name':'A', 'score': 50},
    {'Name':'B', 'score': 60},
    {'Name':'C', 'score': 85},
    {'Name':'D', 'score': 80},
    {'Name':'E', 'score': 90}
]

rank = ['Gold', 'Silver', 'Bronze']

sorted_obj = dict(player) 
sorted_obj = sorted(player, key=lambda x : x['score'], reverse=True)

for i in range(0, len(sorted_obj)):
    if i == 0:
        sorted_obj[i]['rank'] = 'Gold'
    elif i == 1:
        sorted_obj[i]['rank'] = 'Silver'
    elif i == 2:
        sorted_obj[i]['rank'] = 'Bronze'
    else:
        sorted_obj[i]['rank'] = '-'

print(sorted_obj)

# ผลลัพธ์
# [
#     {'Name': 'E', 'score': 90, 'rank': 'Gold'}, 
#     {'Name': 'C', 'score': 85, 'rank': 'Silver'}, 
#     {'Name': 'D', 'score': 80, 'rank': 'Bronze'}, 
#     {'Name': 'B', 'score': 60, 'rank': '-'}, 
#     {'Name': 'A', 'score': 50, 'rank': '-'}
# ]
