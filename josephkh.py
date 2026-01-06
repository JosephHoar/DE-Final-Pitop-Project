# Write your code here :-)
from time import sleep
from pitop import Pitop, Button, LED, LightSensor, SoundSensor, Buzzer
pitop = Pitop()
screen = pitop.miniscreen
led = LED("D4")
led2 = LED("D5")
led3 = LED("D6")
button = Button("D7")
ls = LightSensor("A2")
ss = SoundSensor("A3")
bz = Buzzer("D0")
active = False
setLight = -1
setSound = -1
lrange = -1
srange = -1
set = False
alert = False
while not screen.cancel_button.is_pressed:
    while active and set == False and alert == False:
        led3.on()
        screen.display_text("Active")
        while setLight == -1 or setSound == -1 or lrange == -1 or srange == -1:
            if button.is_pressed:
                active = False
            setLight = int(input("Enter the light control value"))
            setSound = int(input("Enter the sound control value"))
            lrange = int(input("Enter the light range"))
            srange = int(input("Enter the sound range"))
        if setLight != -1 and setSound != -1 and lrange != -1 and srange != -1:
            set = True
        if button.is_pressed:
            active = False
    while active and set and alert == False:
        led2.on()
        lv = ls.reading
        sv = ss.reading
        message = f"Set lv: {lv} sv: {sv}"
        screen.display_text(message)
        if lv > setLight + lrange or lv < setLight - lrange:
            sleep(0.5)
            alert = True
        if sv > setSound + srange or sv < setSound - srange:
            sleep(0.5)
            alert = True
        if button.is_pressed:
            active = False
            set = False
            setLight = -1
            setSound = -1
            lrange = -1
            srange = -1
            sleep(0.5)
        sleep(0.1)
    while active and alert and set:
        led.on()
        lv = ls.reading
        sv = ss.reading
        message = f"Alert lv: {lv} sv: {sv}"
        screen.display_text(message)
        bz.on()
        if lv < setLight + lrange and lv > setLight - lrange and sv < setSound + srange and sv > setSound - srange:
            sleep(0.5)
            alert = False
            led.off()
            bz.off()
        if button.is_pressed:
            active = False
            set = False
            alert = False
            setLight = -1
            setSound = -1
            lrange = -1
            srange = -1
            sleep(0.5)
            bz.off()
        sleep(0.1)
    while active == False:
        screen.display_text("Idle")
        led2.off()
        led.off()
        led3.off()
        if button.is_pressed:
            active = True
            sleep(0.5)