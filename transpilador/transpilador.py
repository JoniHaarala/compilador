def transpiler(p, code_generator, pin=False, is_Pin=False, is_Reserved=False, reserved=False):
    with open("test.ino", "r") as fileRead:
        file = fileRead.readlines()
    with open("test.ino", "w") as fileWrite:
        if p:
            if pin:
                if is_Pin:
                    file += ['void setup(){\n'] + ['\n'] + ['}\n']
                index = file.index('\n')
                file.insert(index, code_generator(p))
                fileWrite.write("".join(file))
                return
            elif reserved:
                if is_Reserved:
                    file += ['loop setup(){\n'] + ['\n'] + ['}\n']
                index = file.index('\n', file.index('\n') + 1)
                file.insert(index, code_generator(p))
                fileWrite.write("".join(file))
                return
            else:
                pass
            file.append(code_generator(p))
            fileWrite.write("".join(file))
