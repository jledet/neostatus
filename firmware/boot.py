import usb_midi, usb_hid, usb_cdc

# Disable MIDI and HID
usb_midi.disable()
usb_hid.disable()

# Enable console and data serials
usb_cdc.enable(console=True, data=True)
