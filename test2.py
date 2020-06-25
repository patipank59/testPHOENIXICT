# สร้าง function ด้วยภาษาที่ถนัดหาชื่อของ key ใน obj ด้านล่างที่มี value เป็น 'value5'

obj = { 
    "key1": 
    {
        "key2" : "value1",
        "key3" : "value2",
        "key4" : 
        {
            "key5": "value5"
        }
    }
}

def search(value):
    return value['key1']['key4']['key5']

print('result')
print(search(obj))
# result
# 'key5'
