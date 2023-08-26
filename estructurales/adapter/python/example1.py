class MonitorHDMI:
    def hdmi(self):
        print("connected in hdmi port!")

class MonitorUSB:
    def usb(self):
        print("connected in usb port!!")


class HDMIToUSBAdapter(MonitorHDMI):
    def __init__(self, usb_monitor: MonitorUSB) -> None:
        self.usb_monitor = usb_monitor

    def hdmi(self):
        self.usb_monitor.usb()

usb_monitor: MonitorUSB = MonitorUSB()
hdmi_monitor: MonitorHDMI = MonitorHDMI()
adapter: HDMIToUSBAdapter = HDMIToUSBAdapter(usb_monitor)

hdmi_monitor.hdmi()
adapter.hdmi()
