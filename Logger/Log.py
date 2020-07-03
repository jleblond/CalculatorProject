import sys
import traceback
from datetime import datetime
from tkinter import messagebox

def start():
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - Starting Application:\n")
        fo.close()
    except FileNotFoundError as e:
        errorETERNITY(e)
    except IOError as e:
        errorETERNITY(e)
    except Exception as e:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")

def end():
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - Closing Application\n")
        fo.close()
    except FileNotFoundError as e:
        errorETERNITY(e)
    except IOError as e:
        errorETERNITY(e)
    except Exception as e:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")


def stdEntry(line):
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - " + str(line) + "\n")
        fo.close()
    except FileNotFoundError as e:
        errorETERNITY(e)
    except IOError as e:
        errorETERNITY(e)
    except Exception as e:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")

def successCalc(entry, total):
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - SUCCESS - USER: "+entry+" = "+ total + "\n")
        fo.close()
    except FileNotFoundError as e:
        errorETERNITY(e)
    except IOError as e:
        errorETERNITY(e)
    except Exception as e:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")

def errorCalc(entry, e):
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - ERROR - USER: " + entry + " : " + str(e.args[0]) + "\n")
        fo.close()
    except FileNotFoundError as e:
        errorETERNITY(e)
    except IOError as e:
        errorETERNITY(e)
    except Exception as e:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")

def errorETERNITY(e):
    try:
        fo = open("log.txt", 'a', encoding = "utf-8")
        fo.write(str(datetime.now()) + " - ERROR - SYSTEM/ETERNITY: " + str(e.args[0]) + "\n")
        fo.close()
    except:
        criticalETERNITY(e, "Unknown Error, ETERNITY will attempt to create an error log and terminate")


def criticalETERNITY(e, message = ""):
    if len(message) == 0:
        alert(0, "Unknown Error, ETERNITY will attempt to create an error log and terminate")
    else:
        alert(0,message)
    try:
        f = "CRASH LOG "+str(datetime.now()).replace(':','')+".txt"
        fo = open(f, 'w')
        traceback.print_exc(None,fo,True)
        fo.close()
        alert(0, "Error Log Created")
    except:
        alert(1, "Fatal Error, ETERNITY was not able to create an error log")
    finally:
        exit(-1)


def alert(type, message):
    if type == 0:
        messagebox.showwarning("Critical Error", message)
    else:
        messagebox.showerror("Critical Error", message)
'''
def clearLog():
    size = os.path.getsize("log.txt")
    if size > 8096: 
        os.remove("log.txt")
    '''