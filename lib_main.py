from tplinkcloud import TPLinkDeviceManager


class LibMain:

    class PowerOfDevice:

        def __init__(self, username='0424002@nkust.edu.tw', password='you850407', device_name="officeHS105"):
            self.username = username
            self.password = password
            self.device_name = device_name
            self.device_manager = TPLinkDeviceManager(self.username, self.password)
            self.device = self.device_manager.find_device(device_name)

        def turn_off_power_device(self):
            if self.device is not None:
                self.device.power_off()
                return True
            else:
                return False

        def turn_on_power_device(self):
            if self.device is not None:
                self.device.power_on()
                return True
            else:
                return False

        def get_current_device_state(self):
            if self.device is not None:
                return self.device.get_sys_info()['state']
            else:
                return "Not found device"
