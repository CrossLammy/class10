members=["admin"]
while True:
    mem=input('กรุณลงชื่อ เพื่อนเล่นเกม หรือ exit เพื่อออก : ').strip()
    if mem == 'exit':
        break
    elif mem in members:
        print('🦄 เริ่มเล่น !!! 🦄')
    else:
        print(f'ไม่พบชื่อ "{mem}" ผู้เล่นไปลงทะเบียนก่อน')

        print('--------register---------')
        new_mem = ''
        while new_mem != 'end':
            new_mem = input('ชื่อที่ต้องการลงทะเบียน หรือ end เพื่อจบการลงทะเบียน : ').strip()
            if new_mem in members:
                print(f'!!! ซ่ำ ลงเทียนไม่ได้ {new_mem}')
            else:
                members.append(new_mem)
        else:
            members.remove('end') # จบ loop while เอา end ออก
        print(members)
print('ไว้เล่นกันใหม่ GG 👾🤺🦾')