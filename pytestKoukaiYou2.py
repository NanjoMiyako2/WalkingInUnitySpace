## function searchBluePerson
##スクリーンショットをとって指定の矩形から青の矩形領域を取得する


import pyautogui as gui
import sys
import time
import cv2
import speech_recognition as sr
import pygetwindow as gw

SAY_FLG_NONE = 1
SAY_FLG_MOVE_FORWARD = 2
SAY_FLG_MOVE_BACKWARD = 3
SAY_FLG_MOVE_LEFT = 4
SAY_FLG_MOVE_RIGHT = 5
SAY_FLG_ROTATE_LEFT = 6
SAY_FLG_ROTATE_RIGHT = 7
SAY_FLG_ROTATE_UP = 8
SAY_FLG_ROTATE_DOWN = 9

print("test100")

g_width = 640;
g_height = 360;

#カメラのサイズを適宜変更して処理速度を調整
g_width2 = 640;
g_height2 = 360;

out_img = cv2.imread("C:\\hogehoge\\white.png");

#out_img = cv2.resize(out_img, (g_width2, g_height2))


timeStart = 0
timeEnd = 0
spanTime = 0

args = sys.argv

print(len(sys.argv))

if len(args) < 2:
 exit()
 
#差分判定率
DiffJudgePercent = float(args[1])

# VideoCapture オブジェクトを取得します
g_capture = cv2.VideoCapture(0)

print(g_capture.set(cv2.CAP_PROP_FRAME_WIDTH, g_width2))
print(g_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, g_height2))
 
print(g_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(g_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


ExecFlg = SAY_FLG_NONE;


def calcWhiteRate(img1):

    global g_width2
    global g_height2
    
    WCount = 0
    
    for x in range(0, g_width2) :
         for y in range(0, g_height2) :
             
             if ( img1[y, x, 0] == 255 and
                  img1[y, x, 1] == 255 and
                  img1[y, x, 2] == 255 ) :
                    WCount = WCount+1
    
    WRate = WCount / (g_width2 * g_height2)
    WRate = WRate * 100.0
    
    return WRate

def Diff(img1, img2):
    
    global g_width2
    global g_height2
    global out_img

    for x in range(0, g_width2) :
         for y in range(0, g_height2) :
            if img1[y, x, 0] >= img2[y, x, 0]:
                out_img[y, x, 0] = abs(img1[y, x, 0] - img2[y, x, 0]);
            else:
                out_img[y, x, 0] = abs(img2[y, x, 0] - img1[y, x, 0]);

            if img1[y, x, 1] >= img2[y, x, 1]:
                out_img[y, x, 1] = abs(img1[y, x, 1] - img2[y, x, 1]);
            else:
                out_img[y, x, 1] = abs(img2[y, x, 1] - img1[y, x, 1]);

            if img1[y, x, 2] >= img2[y, x, 2]:
                out_img[y, x, 2] = abs(img1[y, x, 2] - img2[y, x, 2]);
            else:
                out_img[y, x, 2] = abs(img2[y, x, 2] - img1[y, x, 2]);

            absSum = int(out_img[y, x, 0]) + int(out_img[y, x, 1]) + int(out_img[y, x, 2])
            if absSum >= 120:
                    out_img[y, x, 0] = 255
                    out_img[y, x, 1] = 255
                    out_img[y, x, 2] = 255
            else:
                    out_img[y, x, 0] = 0
                    out_img[y, x, 1] = 0
                    out_img[y, x, 2] = 0
                    
    return out_img

    

def MoveLeft():
    print("左")
    gui.write("0");
    return
    
def MoveRight():
    print("右")
    gui.write("1");
    return
    
def MoveForward():
    print("前")
    gui.write("2");
    return
    
def MoveBackward():
    print("後ろ")
    gui.write("3");
    return
    
def RotateRight():
    print("右回転")
    gui.write("5");
    return
    
def RotateLeft():
    print("左回転")
    gui.write("4");
    return
    
def RotateUp():
    print("上回転");
    gui.write("6");
    return
    
def RotateDown():
    print("下回転");
    gui.write("7");
    return
    

print("start3")

def selectFlg(text):

    flg = SAY_FLG_NONE
    
    if text.find("移動") != -1:
        if text.find("前") != -1 or text.find("前進") != -1:
            flg = SAY_FLG_MOVE_FORWARD;
        
        elif text.find("後ろ") != -1 or text.find("後退") != -1:
            flg = SAY_FLG_MOVE_BACKWARD;
            
        elif text.find("右") != -1:
            flg = SAY_FLG_MOVE_RIGHT;
            
        elif text.find("左") != -1:
            flg = SAY_FLG_MOVE_LEFT;
                    

    elif text.find("回転") != -1 or text.find("開店") != -1:
        if text.find("上") != -1:
            flg = SAY_FLG_ROTATE_UP;
            
        elif text.find("下") != -1 or text.find("舌") != -1:
            flg = SAY_FLG_ROTATE_DOWN;
            
        elif text.find("右") != -1:
            flg = SAY_FLG_ROTATE_RIGHT;
                
        elif text.find("左") != -1:
            flg = SAY_FLG_ROTATE_LEFT;
    
    
    return    flg


def getSayWord(q_text):
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print(q_text)
        audio = r.listen(source)

    text = r.recognize_google(audio, key=None, language='ja-JP')

    print("発話文:"+text)
    
    return text




def Play():

    global g_capture
    global g_width
    global g_height

    global out_img
    global WalkFlg
    global DiffJudgePercent
    
    global MatchCount
    global ExecFlg
    
    

    
    timeStart = 0.0
    timeEnd = 0.0
    spanTime = 0.0
    timeSpan = 0.1;

    StopCount = 0
    
    ExecFlg = SAY_FLG_NONE
    
    breakFlg = False;
    WalkFlg = False;
    while True:
        print("qを押して終了")

        ret, frame = g_capture.read()
        img1 = frame;

        cv2.imshow('frame', frame)
        
        while WalkFlg == False:
            gui.click(1400, 180)
            text1 = getSayWord("何か発話してください(「終了」で終了)")
            if text1.find("終") != -1:
                breakFlg = True;
                break
            
            print(gui.position())
                
            text2 = getSayWord("以下の発話でよい場合は「OK」と言ってください(「もう一度」でもう一度発話")
            
            if text2.find("OK") != -1:
                WalkFlg = True;
                ExecFlg = selectFlg(text1)
                time.sleep(5)
                print("aaa")
                break
                
        
        if breakFlg == True:
            break


        execute(ExecFlg)
        gui.click(1400, 180)
        
        str1 = cv2.waitKey(1)
                
        if str1 == ord("q"):
            break
            
        currentTime = time.time()
        if timeStart == 0:
            timeStart = time.time()
            timeEnd = time.time()
            img2 = img1
            
        else:
            timeEnd = time.time()
            
        timeDiff = timeEnd - timeStart
        
        if(timeDiff >= timeSpan):
            img3 = Diff(img1, img2)
            WRate = calcWhiteRate(img3)
            print(WRate)
            if WRate >= DiffJudgePercent:
                StopCount = 0
                WalkFlg = True
                print("walkFlg:True");
                
            else:
                if StopCount >= 3:
                    WalkFlg = False
                    StopCount = 0
                else:
                    StopCount = StopCount + 1
                    
                print("walkFlg:False")

            timeStart = currentTime
       
        img2 = img1
    
    g_capture.release()

    cv2.destroyAllWindows()
    
    return

def execute(ExecFlg):
    
    gui.click(420,570)
    
    

    if SAY_FLG_NONE == ExecFlg:
        return
    elif SAY_FLG_MOVE_FORWARD == ExecFlg:
        MoveForward()
        
    elif SAY_FLG_MOVE_BACKWARD == ExecFlg:
        MoveBackward()
        
    elif SAY_FLG_MOVE_LEFT == ExecFlg: 
        MoveLeft()
        
    elif SAY_FLG_MOVE_RIGHT == ExecFlg:
        MoveRight()
        
    elif SAY_FLG_ROTATE_LEFT == ExecFlg:
        RotateLeft()
        
    elif SAY_FLG_ROTATE_RIGHT == ExecFlg:
        RotateRight()
        
    elif SAY_FLG_ROTATE_UP == ExecFlg:
        RotateUp()
        
    elif SAY_FLG_ROTATE_DOWN == ExecFlg:
        RotateDown()
        
        
    return

def main(): 

    Play()


    return 0
   

    
        
main()

    