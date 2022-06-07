import pyautogui
import time

#計算手勢時長
savetime=0
savetext='non'
def maintenance_time(text):
    global savetext ,savetime
    now=time.time()
    if text=='':      #檢測是否沒比動作
        savetime=0
        savetext=''
        return ''

    elif savetext!=text: #檢查是不是一樣的字
        savetime=now
        savetext=text
        return 0
    
    else:
        longtime=now-savetime
        if longtime>1:
            if text=='1' or text=='2' or text=='3' or text=='4' or text=='5' or text=='6' or text=='7' or text=='8' or text=='9'or text=='0':
                pyautogui.hotkey('num'+text)
            elif text=='good':
                pyautogui.hotkey('enter')
            elif text=='no!!!':
                pyautogui.hotkey('alt', 'f4')
            elif text=='ROCK!':
                pyautogui.hotkey('R', 'O','C','K','!','!')
            savetime=now
            return longtime

# 手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50: #大拇指
        return 'good'
    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50: #中指
        return 'no!!!'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50: 
        return 'ROCK!'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return '0'
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '2'
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return '3'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '4'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '5'
    elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return '6'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '7'
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '8'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
        return '9'
    else:
        return ''


