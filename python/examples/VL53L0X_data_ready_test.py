import time
import vl53l0x

tof = vl53l0x.VL53L0X(tca9548a_num=1, tca9548a_addr=0x70)
tof.connect()
tof.start_ranging(vl53l0x.Vl53l0xAccuracyMode.BEST)

tic = time.time()
while True:
    try:
        if tof.data_ready:
            print(
                f"\rDistance = {tof.get_data()};"
                f"Time = {time.time() - tic}",
                end=""
            )
            tic = time.time()
    except KeyboardInterrupt:
        break

tof.stop_ranging()
tof.disconnect()
