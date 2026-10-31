# в 2 раза быстрее
import pyautogui
import keyboard
import cv2
import time
def painter():
    start_time = time.perf_counter()
    print(f"начало работы пеинтера\nволучено {len(sceth)} точек")
    start_P = pyautogui.position()
    W_start, H_start = start_P
    for kord in sceth:
        kord_2 = kord.strip('()').split(',')
        x = int(kord_2[0])
        y = int(kord_2[1])
        
        pyautogui.click(W_start + y , H_start + x)
    end_time = time.perf_counter()
    print(f"конец работы пеинтера время работы составило {end_time - start_time:.4f}")


def chek_img():
    sceth = []
    start_time = time.perf_counter()
    img = cv2.imread('1.png',0)
    height, width = img.shape
    size = height*width
    print(f"Размер: {width}x{height}\nПикселей: {size}")
    for y in range(height):       # range(192)
        for x in range(width):    # range(256)
            pixel = img[y, x] 
            if pixel == 255:
                sceth.append(f'{y,x}')
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f'Время выполнения считывания {execution_time:.4f} секунд(ы)\nнайдено {len(sceth)}точек\n\n')
    return(sceth)
sceth =chek_img()
keyboard.add_hotkey('alt+z', chek_img)
keyboard.add_hotkey('alt+x', painter)
keyboard.wait('esc')
