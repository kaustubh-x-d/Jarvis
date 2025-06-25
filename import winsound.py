import winsound

# Play a system default notification sound
winsound.MessageBeep()

# Wait a moment (optional)
import time
time.sleep(0.5)

# Play a custom beep: 1000 Hz tone for 500 milliseconds
winsound.Beep(1000, 500)
