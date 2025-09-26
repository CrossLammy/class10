import junken
members = ['admin']

def check_name(name):
    if name in members:
        return True
    else:
        return False

def play_game(themem):
    print('--------- Play Game ---------')
    print(f'🦄 เริ่มเล่น !!! 🦄 {themem}')
    junken.start()

def reg():
    print('-------- register ---------')
    new_mem = ''
    while new_mem != 'end':
        new_mem = input('ชื่อที่ต้องการลงทะเบียน หรือ end เพื่อจบการลงทะเบียน : ').strip()
        if check_name(new_mem):
            print(f'!!! ซ่ำ ลงเทียนไม่ได้ {new_mem}')
        else:
            members.append(new_mem)
    else:
        members.remove('end') # จบ loop while เอา end ออก
    print(members)

#main
while True:
    mem=input('กรุณลงชื่อ เพื่อนเล่นเกม หรือ exit เพื่อออก : ').strip()
    if mem == 'exit':
        break
    elif check_name(mem):
        play_game(mem)
    else:
        print(f'ไม่พบชื่อ "{mem}" ผู้เล่นไปลงทะเบียนก่อน')
        reg()