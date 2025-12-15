#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from math import ceil
from time import sleep, strftime
from random import randint, randrange, choice
from subprocess import run, Popen, PIPE, STDOUT


def fuzz(content, factor, ascii_bytes=False):
    """Fuzz data with random bytes.

    :param content: data to fuzz
    :param factor: maximum proportion of the data that can change
    :param ascii_bytes: whether the random bytes should be valid ascii characters
    :return: fuzzed buffer
    """
    buffer = bytearray(content)

    n_writes = randint(1, ceil(len(buffer) * factor))
    for i in range(n_writes):
        rand_byte = randint(32, 126) if ascii_bytes else randrange(256)
        rand_pos = randrange(len(buffer))
        buffer[rand_pos] = rand_byte

    return bytes(buffer)


def clear_screen():
    """Clear the console screen in a portable way."""
    os.system('clear' if os.name == 'posix' else 'cls')


def main():
    # Config
    input_dir = 'input/dpsm/'
    output_dir = 'crashes/'
    fuzz_output = 'testfile'
    apps = [
        ['./dpsm.py', '--verbose', fuzz_output, '/dev/null'],  # cf. presentation.pdf
        # ['ristretto', fuzz_output],
        # ['vlc', fuzz_output],
        # ['atril', fuzz_output],
        # ['libreoffice', fuzz_output]
    ]
    n_tests = 10000
    timeout = 0
    fuzz_factor = 0.001
    ascii_bytes = True

    # Setup
    input_files = os.listdir(input_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Test
    n_crashes = 0
    for i in range(n_tests):
        # Choose a random app and file
        app = choice(apps)
        file_name = choice(input_files)

        # Fuzz the file
        with open(os.path.join(input_dir, file_name), 'rb') as file:
            content = file.read()

        with open(fuzz_output, 'wb') as file:
            file.write(fuzz(content, fuzz_factor, ascii_bytes=ascii_bytes))

        # Open it with the chosen app
        clear_screen()
        print(f'Test {i + 1} of {n_tests} (crashes: {n_crashes})\n'
              f'app={app}\n'
              f'file_name={file_name}\n'
              f'timeout={timeout}\n'
              f'fuzz_factor={fuzz_factor}\n'
              f'ascii_bytes={ascii_bytes}\n')

        if timeout:
            process = Popen(app, encoding="utf-8", stdout=PIPE, stderr=STDOUT)
            sleep(timeout)
            crashed = process.poll()
            if not crashed:
                process.terminate()

        else:
            process = run(app, encoding="utf-8", stdout=PIPE, stderr=STDOUT)
            crashed = process.returncode

        # If it crashed, save the test case and its output
        if crashed:
            n_crashes += 1
            crash_name = os.path.join(output_dir, f'{strftime("%Y-%m-%d.%H-%M-%S")}.{i}.{file_name}')
            
            os.rename(fuzz_output, crash_name)
            with open(crash_name + '.log', 'w') as file:
                file.write(process.stdout)

    # Done
    os.remove(fuzz_output)  # clean up
    print('Done\n'
          f'Successes: {n_tests - n_crashes}\n'
          f'Crashes: {n_crashes} ({ceil(n_crashes/n_tests * 10000) / 100}%)')


if __name__ == '__main__':
    main()
