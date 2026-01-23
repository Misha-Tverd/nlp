import config
import processors
import io_utils

def main():
    print(io_utils.read(config.INPUT_TXT))
    data = processors.main()
    print(data)


main()