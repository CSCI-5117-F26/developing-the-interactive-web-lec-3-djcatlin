from halo import Halo
import time

def main() -> None:
    spinner = Halo(text='Spinning', spinner='dots')
    spinner.start()

    time.sleep(60)
    spinner.stop()
