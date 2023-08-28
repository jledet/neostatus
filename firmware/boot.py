import usb_midi
import usb_hid
import usb_cdc
import storage
import microcontroller

# Disable MIDI and HID
usb_midi.disable()
usb_hid.disable()

# Disable console and enable data serials
usb_cdc.enable(console=True, data=True)

# Disable storage unless startup_mode is non-zero:
startup_mode = microcontroller.nvm[0]
if startup_mode != 0:
    microcontroller.nvm[0] = 0
else:
    storage.disable_usb_drive()
