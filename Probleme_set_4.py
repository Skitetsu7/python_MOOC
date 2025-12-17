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


def main():
    # Config
    directory_de_base = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(directory_de_base, "input")          
    output_dir = os.path.join(directory_de_base, "crashes")        
    fuzz_output = os.path.join(directory_de_base, "testfile.txt") 
    libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"  # adress modifier

    apps = [
        [libreoffice_path, fuzz_output],
        #[r"%HOMEDRIVE%%HOMEPATH%%windir%\system32\notepad.exe", fuzz_output],
    ]
    n_tests = 10 000 #n_tests est tester pour à chaque itération le test aléatoire
    # chaque itération consiste à choisir un fichier au hazard, le 'fuzzer' en modifiant des octets, lancer l'app sur le fichier er cerifier les crash
    # crash assez rare du coup faut dépasser les 100, plus le n_tests est grand plus la confiance augmente envers le code pour résister au crash potentiel 
    timeout = 2 #delai pour laisser au programme le temps de reagir
    fuzz_factor = 0.01 #1% du fichier sert de correction du facteur (au lieu des 250 de base)
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
        print(f'Test {i + 1} of {n_tests} (crashes: {n_crashes})\n'
              f'app={app}\n'
              f'file_name={file_name}\n'
              f'timeout={timeout}\n'
              f'fuzz_factor={fuzz_factor}\n'
              f'ascii_bytes={ascii_bytes}\n')

        if timeout:
            process = Popen(app, encoding="utf-8", stdout=PIPE, stderr=STDOUT, shell= True) #shell= True parce que windows a un problème avec les espaces et il y a un espaces dans mon fichier
            sleep(timeout)
            crashed = process.poll()
            if crashed is None:
                process.terminate()
            elif crashed !=0: #crash si le code est différent de 0
                n_crashes+=1
                crash_name =os.path.join(output_dir, f'{strftime("%Y-%m-%d.%H-%M-%S")}.{i}.{file_name}')
                os.rename(fuzz_output, crash_name)
                with open(crash_name+ '.log', 'w') as file:
                    file.write(process.stdout)
        else:
            process = run(app, encoding="utf-8", stdout=PIPE, stderr=STDOUT)
            crashed = process.returncode  # return the error of the app if it crashed

            # If it crashed, save the test case and its output
            if crashed !=0:
                n_crashes += 1
                crash_name = os.path.join(
                    output_dir, f'{strftime("%Y-%m-%d.%H-%M-%S")}.{i}.{file_name}')  # Create a name for the crash file for the archives

                os.rename(fuzz_output, crash_name)
                with open(crash_name + '.log', 'w') as file:  # Create a log file
                    # Write the output of the app in the log file
                    file.write(process.stdout)

    # Done
    if os.path.exists(fuzz_output): #eviter l'erreur si le fichier a été renommer
        os.remove(fuzz_output) #neccessaire pour pas saturé le disque dur
    print('Done\n'
          # print the number of successes
          f'Successes: {n_tests - n_crashes}\n'
          f'Crashes: {n_crashes} ({ceil(n_crashes/n_tests * 10000) / 100}%)')  # Print the number of crashes and the percentage of crashes


if __name__ == '__main__':
    main()
