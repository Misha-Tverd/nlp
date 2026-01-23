import config
import processors
import io_utils

def main():
    text = io_utils.read(config.INPUT_TXT)
    data = processors.main(text)
    change_result = io_utils.format_result(data)
    print(change_result)
    output_txt = config.OUTPUT_TXT

    io_utils.write(output_txt, change_result)
    print(io_utils.read(config.OUTPUT_TXT))

main()