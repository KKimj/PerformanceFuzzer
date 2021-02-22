import argparse


def main(filename_list, option_list):
    # print('Target File : {}'.format(filename_list))
    # print(filename_list)
    # print('Optional : {}'.format(option_list))
    nop_count = 1

    file_opt_ll = open("./tests/"+filename_list[0]+"_opt.ll", "r")
    file_fuz_ll = open("./tests/"+filename_list[0]+"_opt_fuzzer.ll", "w")
    
    while True:
        line = file_opt_ll.readline()
        file_fuz_ll.write(line)
        if not line:
            break
        if line.startswith("; <label>") and nop_count > 0:
            file_fuz_ll.write('  call void asm sideeffect "NOP;", ""()\n')
            nop_count -= 1
            
        print(line)

    file_opt_ll.close()
    file_fuz_ll.close()



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs='+' ,help='Example) index.html', dest='filename')
    parser.add_argument('--optional', '-o', nargs='*', help='Example) save', default=[], dest='option')

    filename_list = parser.parse_args().filename
    option_list = parser.parse_args().option

    return filename_list, option_list


if __name__ == '__main__':
    filename_list, option_list = get_arguments()
    main(filename_list, option_list)