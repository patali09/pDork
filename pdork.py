import subprocess
try:
    from selenium import webdriver
except:
    subprocess.run("sudo pip3 install selenium", shell=True)
    from selenium import webdriver
try:
    driver = webdriver.Firefox()
except:
    subprocess.run("wget -o geckdriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && tar –xvzf geckdriver.tar.gz && sudo mv geckodriver /usr/bin", shell=True)
    driver = webdriver.Firefox()
target = input("Enter the target domain: ")
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
    20:{".htaccess sensitive files ":'site:{target} inurl:"/phpinfo.php" | inurl:".htaccess"'},
    21:{"Find WordPress #2 ":' site:{target} inurl:wp":"content | inurl:wp":"includes"'},
    22:{"Search in GITHUB ":" https://github.com/search?q=%22*.{target}%22"},
    23:{"Search in OpenBugBounty ":" https://www.openbugbounty.org/search/?search={target}"},
    24:{"Test CrossDomain ":" {target}/crossdomain.xml"},
    25:{".gt folder ":' inurl:"/.git "{target} ":"github"'},
    26:{"Find .SWF file (Google) ":" inurl:{target} ext:swf"},
    26:{"Find .SWF file (Yandex) ":" site:{target} mime:swf  (https://yandex.com/search/?text=site%3A{target}%20%20mime%3Aswf&lr=10613)"},
    27:{"Traefik ":'intitle:traefik inurl:8080/dashboard"{target}"'},
    28:{"s3 Bucets ":'site:.s3.amazonaws.com "{target}"'},
    29:{"Sourcecode PublicWWW":' https://publicwww.com/websites/%22{target}%22/'},
    30:{'CVE-2020-0646 SharePointRCE':".sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec site:{target.com}"},
    31:{"API Endpoints WSDL" : 'site:{target.com} filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl'},
    32:{"Github GIST Searches" : "https://gist.github.com/search?q=*.%22{target.com}%22"},
    33:{"Plaintext Password Leak": "site:throwbin.io {target.com}"}
}


for inputs in range(1 , 34):
    for i in dorks:
        dork = list(dorks)
        name = list(dorks[dork[inputs-1]])
        key = name[0]
        print(str(inputs) +" : "+ key)

        break

while True:
    dork_num = input("Enter the dork number: ")
    if (dork_num == "exit"):
        driver.quit()
        break
    elif (dork_num==""):
        print("Sorry enter correct value")
    else:
        dork = list(dorks)
        name = list(dorks[dork[int(dork_num)-1]])
        key = name[0]
        new_dork = dorks[int(dork_num)][key].replace("{target}", target)
        driver.get(f"https://www.google.com/search?q={new_dork}")


    