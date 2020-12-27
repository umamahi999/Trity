    os.system('apt-get install python-pip')

    os.system('easy_install pip')

    import pip

    os.system('sudo apt-get install libjpeg-dev libfreetype6 zlib1g-dev')

    os.system('pip2.7 install --upgrade beautifulsoup4')

    os.system('pip install google')

    os.system('pip install requests')

    os.system('pip install pythonwhois')

    os.system('pip2.7 install --upgrade html5lib')

    os.system('pip install pillow')

    os.system('pip install qrcode')

    os.system('pip install requests[security]')

@@ -41,7 +44,7 @@

    install2 = os.system("cp -R trity/ /opt/ && cp trity.py /opt/trity && cp run.sh /opt/trity && cp run.sh /usr/bin/trity && chmod +x /usr/bin/trity")

    os.system('apt-get install sendemail')

    os.system('apt-get install libncurses5')

    pip.main(["install", "scapy", "SpoofMAC", "pythonwhois", "BeautifulSoup", "requests", "mechanize", "google", "qrcode"])

    pip.main(["install", "scapy", "pythonwhois", "BeautifulSoup", "requests", "mechanize", "google", "qrcode"])

    print "\033[1;32m[!] Finished Installing! Run 'trity' to run program [!]\033[0m"

    sys.exit()

else:

    print "Whoops! Something went wrong!"
