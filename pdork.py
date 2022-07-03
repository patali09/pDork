#!/usr/bin/python3
import subprocess
import argparse
pars = argparse.ArgumentParser()
pars.add_argument('-d', type=str)
pars.add_argument('-l', type=str)
args = pars.parse_args()
try:
    from selenium import webdriver
except:
    print("______First Install Python Selenium _____")
    quit()
try:
    subprocess.run("figlet pDork", shell=True)
    print("                                                 By Patali")
except:
    pass
driver = webdriver.Firefox()

dorks = {
    1:{"Directory Listing":" site:{target} intitle:index.of"},
    2:{"Configuration Files ":" site:{target} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"},
    3:{"Database Files":" site:{target} ext:sql | ext:dbf | ext:mdb"},
    4:{"WordPress":" site:{target} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"},
    5:{"Log Files":"site:{target} ext:log"},
    6:{"Backup and Old Files":"site:{target} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"},
    7:{"Login Pages":"site:{target} inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth"},
    8:{"SQL Errors":'site:{target} intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'},
    9:{"Apache Connfig FIles":'site:{target} filetype:config "apache"'},
    10:{"Robots.txt File":"{target}/robots.txt"},
    11:{"Publicly Eposed Documents":"site:{target} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"},
    12:{"phpinfo{}":'site:{target} ext:php intitle:phpinfo "published by the PHP Group"'},
    13:{"Finding Backdoors":"site:{target}  inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor"},
    14:{"Install / Setup Files":"site:{target}  inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config"},
    15:{"Open Redirects":" site:{target} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http"},
    16:{"Apache STRUTS RCE":"site:{target} ext:action | ext:struts | ext:do"},
    17:{"GitLab":"inurl:gitlab {target}"},
    18:{"Find Pastenin entries ":" site:pastebin.com {target}"},
    19:{"Employees on LINKDIIN ":" site:linkedin.com employees {target}"},
    20:{".htaccess sensitive files ":'site:{target} inurl:"phpinfo.php" | inurl:".htaccess"'},
    21:{"Find WordPress #2 ":' site:{target} inurl:wp":"content | inurl:wp":"includes"'},
    22:{"Test CrossDomain ":" {target}/crossdomain.xml"},
    23:{".gt folder ":' inurl:"/.git "{target} ":"github"'},
    24:{"Find .SWF file (Google) ":" inurl:{target} ext:swf"},
    25:{"Traefik ":'intitle:traefik inurl:8080/dashboard    "{target}"'},
    26:{"s3 Bucets ":'site:.s3.amazonaws.com "{target}"'},
    27:{'CVE-2020-0646 SharePointRCE':".sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec site:{target} "},
    28:{"API Endpoints WSDL" : 'site:{target} filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl'},
    29:{"Plaintext Password Leak": "site:throwbin.io {target}"}
}

 

for inputs in range(1, len(dorks)+1):
    for i in dorks:
        dork = list(dorks)
        name = list(dorks[dork[inputs-1]])
        key = name[0]
        print(str(inputs) +" : "+ key)
        break


def single_domain():
    print("[*] Current target is "+ target)
    while True:
        dork_num = input("Enter the dork number: ")
        if (dork_num.isalnum()):
            if (dork_num=="exit"): 
                if (dork_num == "exit"):
                    driver.quit()
                    quit()
                else:
                    continue
            try:
                if (len(dorks) >= int(dork_num)):
                    if (dork_num=='10'):
                        driver.get(f"https://{target}/robots.txt")
                    else:
                        dork = list(dorks)
                        name = list(dorks[dork[int(dork_num)-1]])
                        key = name[0]
                        new_dork = dorks[int(dork_num)][key].replace("{target}", target)
                        driver.get(f"https://www.google.com/search?q={new_dork}")
                else:
                    print(f"\nSorry, Wrong Dork Number or Wrong Command\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> exit")
            except:
                    print(f"\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> exit")
        else:
            print("[*] Invalid Command")
            print(f"\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> exit")


def multi_domain():
    with open(args.l, "r") as targets:
        domains = targets.readlines()
        for target in domains:
            if (target.startswith("http://") or target.startswith("https://")):  #to remove https or http if target list starts with it
                try:
                    target = target.removeprefix("https://")
                except NameError:
                    target = target.removeprefix("http://")
                except:
                    print(f"{target[:-1]} starts with protocts other thant http or https. \n \t ERROR_______ERROR______ERROR\n_____SKIPPING____")
                    break
                print("\n\t[*] Current target is: "+ target)
            while True:
                num = 1
                dork_num = input("Enter the dork number: ")
                if (dork_num.isalnum()):
                    if ((dork_num=="next") or ((dork_num=="exit") or (dork_num=="print"))): 
                        if (dork_num == "exit"):
                            driver.quit()
                            quit()
                        elif(dork_num=="next"):
                            print("[*] Skipping current target "+ target[:-1])
                            break
                        elif(dork_num=="print"):
                            for i in domains:
                                print(f"{num} : {i[:-1]}")
                                num+=1
                                pass
                        else:
                            continue
                    try:
                        if (len(dorks) >= int(dork_num)):
                            if (dork_num=='10'):
                                driver.get(f"https://{target}/robots.txt")
                            else:
                                dork = list(dorks)
                                name = list(dorks[dork[int(dork_num)-1]])
                                key = name[0]
                                new_dork = dorks[int(dork_num)][key].replace("{target}", target)
                                driver.get(f"https://www.google.com/search?q={new_dork}")
                        else:
                            print(f"\nSorry, Wrong Dork Number or Wrong Command\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> next\n\t--> print\n\t--> exit")
                    except:
                            print(f"\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> next\n\t--> print\n\t--> exit")
                else:
                    print("[*] Invalid Command")
                    print(f"\nValid Commands are: \n\t--> 1 to {len(dorks)}\n\t--> next\n\t--> print\n\t--> exit")


if (args.d ==None):
    multi_domain()
elif (args.l==None):
    target = args.d
    single_domain()
else:
    print("[*] ERROR...............ERROR...............ERROR")
