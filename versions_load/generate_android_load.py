import os
import threading, zipfile, shutil#, cPickle

###############################################

disk_lock = threading.RLock()
f  = open('E:/my_modded_renpy/renpy_modded/TestForRpandaAndroid/game/versions_load/android_load.rpy', 'w', encoding='utf-8')
print('init python:', file = f)
print('    android_load = {', file = f)
for version in ['0.2.1', '0.2.2', '0.2.3', '0.3.1', '0.3.2', '0.3.3', '0.4.1', '0.4.2', '0.4.3']:
    file = 'E:/my_modded_renpy/renpy_modded/TestForRpandaAndroid/game/versions_load/' + version + '.save'
    print(str(version) + ':' + "'''", file = f)

    
    with disk_lock:

        zf = zipfile.ZipFile(file, "r")
        rv = zf.read("log")
        #print('!@!' + str(type(rv)))
                #print(rv)
        zf.close()
        
        print(rv, file = f)

    print("'''", file = f)