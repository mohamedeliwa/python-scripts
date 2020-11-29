#!/usr/bin/env python3
import subprocess
print("start")
username = 'shaun'

# running a command in shell after changing working directory to path
subprocess.run(["./start-tor-browser.desktop"], shell=True,
               cwd=f'/home/{username}/Desktop/tor-browser_en-US')
print("Done")


'''
This script opens Tor Browser on ubuntu:
    assuming that tor browser folder is on the desktop

    it changes the current working directory to the tor browser directory
    then excutes a command in the shell
'''

'''
#!/usr/bin/python3:
    this is A shebang line defines where the interpreter is located.
    In this case, the python3 interpreter is located in /usr/bin/python3.
    A shebang line could also be a bash, ruby, perl or any other scripting languages' interpreter, for example: #!/bin/bash.

#!/usr/bin/env python3:
    do the same as above line.
    but it's more portable and flexible,
    as it Will interpret your $PATH, and find python in any directory in your $PATH.
    so will make sure you run the script with,
    whatever python installed in the current active python virtual environment.
    so it's more better than above line 


'''
'''
making this file excutable by changing permissions
then allowing it to be excuted as programs.
this will allow us to excute its code by double clicking at as we do with any other program
'''