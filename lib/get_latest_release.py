import os

def get_latest():
    os.system('cd ../../catalog;ls | grep 5. >> ../mainline-builder/lib/file1.txt')

    with open('file1.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    con_rc = 'rc'

    def Filter(string, substr):
        return [str for str in string if
                any(sub in str for sub in substr)]

    rc = Filter(content, con_rc)
    notrc = [x for x in content if x not in rc]
    rc59 = [x for x in rc if x.startswith('5.9')]
    rc = [x for x in rc if x not in rc59]

    if [x for x in notrc if x.endswith('.10.10')]:
        lts_remove5101 = lts = [x for x in notrc if x.endswith('.10.1')]
        lts_remove5101 = [x for x in notrc if x not in lts_remove5101]
        lts_remove5102 = lts = [x for x in lts_remove5101 if x.endswith('.10.2')]
        lts_remove5102 = [x for x in lts_remove5101 if x not in lts_remove5102]
        lts_remove5103 = lts = [x for x in lts_remove5102 if x.endswith('.10.3')]
        lts_remove5103 = [x for x in lts_remove5102 if x not in lts_remove5103]
        lts_remove5104 = lts = [x for x in lts_remove5103 if x.endswith('.10.4')]
        lts_remove5104 = [x for x in lts_remove5103 if x not in lts_remove5104]
        lts_remove5105 = lts = [x for x in lts_remove5104 if x.endswith('.10.5')]
        lts_remove5105 = [x for x in lts_remove5104 if x not in lts_remove5105]
        lts_remove5106 = lts = [x for x in lts_remove5105 if x.endswith('.10.6')]
        lts_remove5106 = [x for x in lts_remove5105 if x not in lts_remove5106]
        lts_remove5107 = lts = [x for x in lts_remove5106 if x.endswith('.10.7')]
        lts_remove5107 = [x for x in lts_remove5106 if x not in lts_remove5107]
        lts_remove5108 = lts = [x for x in lts_remove5107 if x.endswith('.10.8')]
        lts_remove5108 = [x for x in lts_remove5107 if x not in lts_remove5108]
        lts_remove5109 = lts = [x for x in lts_remove5108 if x.endswith('.10.9')]
        lts_remove5109 = [x for x in lts_remove5108 if x not in lts_remove5109]
        lts = [x for x in lts_remove5109 if x.startswith('5.10')]
    if [x for x in notrc if x.endswith('.10.11')]:
        lts_remove5101 = lts = [x for x in notrc if x.endswith('.10.1')]
        lts_remove5101 = [x for x in notrc if x not in lts_remove5101]
        lts_remove5102 = lts = [x for x in lts_remove5101 if x.endswith('.10.2')]
        lts_remove5102 = [x for x in lts_remove5101 if x not in lts_remove5102]
        lts_remove5103 = lts = [x for x in lts_remove5102 if x.endswith('.10.3')]
        lts_remove5103 = [x for x in lts_remove5102 if x not in lts_remove5103]
        lts_remove5104 = lts = [x for x in lts_remove5103 if x.endswith('.10.4')]
        lts_remove5104 = [x for x in lts_remove5103 if x not in lts_remove5104]
        lts_remove5105 = lts = [x for x in lts_remove5104 if x.endswith('.10.5')]
        lts_remove5105 = [x for x in lts_remove5104 if x not in lts_remove5105]
        lts_remove5106 = lts = [x for x in lts_remove5105 if x.endswith('.10.6')]
        lts_remove5106 = [x for x in lts_remove5105 if x not in lts_remove5106]
        lts_remove5107 = lts = [x for x in lts_remove5106 if x.endswith('.10.7')]
        lts_remove5107 = [x for x in lts_remove5106 if x not in lts_remove5107]
        lts_remove5108 = lts = [x for x in lts_remove5107 if x.endswith('.10.8')]
        lts_remove5108 = [x for x in lts_remove5107 if x not in lts_remove5108]
        lts_remove5109 = lts = [x for x in lts_remove5108 if x.endswith('.10.9')]
        lts_remove5109 = [x for x in lts_remove5108 if x not in lts_remove5109]
        lts = [x for x in lts_remove5109 if x.startswith('5.10')]
    else: lts = [x for x in notrc if x.startswith('5.10')]

    mainline = [x for x in notrc if x not in lts]

    if [x for x in mainline if x.startswith('5.9')]:
        mainline_remove59 = [x for x in mainline if x.startswith('5.9')]
        mainline_remove59 = [x for x in mainline if x not in mainline_remove59]
        mainline = mainline_remove59


    if [x for x in mainline if x.startswith('5.8')]:
        mainline_remove58 = [x for x in mainline if x.startswith('5.8')]
        mainline_remove58 = [x for x in mainline if x not in mainline_remove58]
        mainline = mainline_remove58

    if [x for x in mainline if x.startswith('5.4')]:
        mainline_remove54 = [x for x in mainline if x.startswith('5.4')]
        mainline_remove54 = [x for x in mainline if x not in mainline_remove54]
        mainline = mainline_remove54

    if [x for x in mainline if x.endswith('.10')]:
        mainline_remove1 = [x for x in mainline if x.endswith('.1')]
        mainline_remove1 = [x for x in mainline if x not in mainline_remove1]
        mainline_remove2 = [x for x in mainline_remove1 if x.endswith('.2')]
        mainline_remove2 = [x for x in mainline_remove1 if x not in mainline_remove2]
        mainline_remove3 = [x for x in mainline_remove2 if x.endswith('.3')]
        mainline_remove3 = [x for x in mainline_remove2 if x not in mainline_remove3]
        mainline_remove4 = [x for x in mainline_remove3 if x.endswith('.4')]
        mainline_remove4 = [x for x in mainline_remove3 if x not in mainline_remove4]
        mainline_remove5 = [x for x in mainline_remove4 if x.endswith('.5')]
        mainline_remove5 = [x for x in mainline_remove4 if x not in mainline_remove5]
        mainline_remove6 = [x for x in mainline_remove5 if x.endswith('.6')]
        mainline_remove6 = [x for x in mainline_remove5 if x not in mainline_remove6]
        mainline_remove7 = [x for x in mainline_remove6 if x.endswith('.7')]
        mainline_remove7 = [x for x in mainline_remove6 if x not in mainline_remove7]
        mainline_remove8 = [x for x in mainline_remove7 if x.endswith('.8')]
        mainline_remove8 = [x for x in mainline_remove7 if x not in mainline_remove8]
        mainline_remove9 = [x for x in mainline_remove8 if x.endswith('.9')]
        mainline_remove9 = [x for x in mainline_remove8 if x not in mainline_remove9]
        mainline = mainline_remove9
    if [x for x in mainline if x.endswith('.11')]:
        mainline_remove1 = [x for x in mainline if x.endswith('.1')]
        mainline_remove1 = [x for x in mainline if x not in mainline_remove1]
        mainline_remove2 = [x for x in mainline_remove1 if x.endswith('.2')]
        mainline_remove2 = [x for x in mainline_remove1 if x not in mainline_remove2]
        mainline_remove3 = [x for x in mainline_remove2 if x.endswith('.3')]
        mainline_remove3 = [x for x in mainline_remove2 if x not in mainline_remove3]
        mainline_remove4 = [x for x in mainline_remove3 if x.endswith('.4')]
        mainline_remove4 = [x for x in mainline_remove3 if x not in mainline_remove4]
        mainline_remove5 = [x for x in mainline_remove4 if x.endswith('.5')]
        mainline_remove5 = [x for x in mainline_remove4 if x not in mainline_remove5]
        mainline_remove6 = [x for x in mainline_remove5 if x.endswith('.6')]
        mainline_remove6 = [x for x in mainline_remove5 if x not in mainline_remove6]
        mainline_remove7 = [x for x in mainline_remove6 if x.endswith('.7')]
        mainline_remove7 = [x for x in mainline_remove6 if x not in mainline_remove7]
        mainline_remove8 = [x for x in mainline_remove7 if x.endswith('.8')]
        mainline_remove8 = [x for x in mainline_remove7 if x not in mainline_remove8]
        mainline_remove9 = [x for x in mainline_remove8 if x.endswith('.9')]
        mainline_remove9 = [x for x in mainline_remove8 if x not in mainline_remove9]
        mainline = mainline_remove9

    # make numbers 
    mainline = [s.replace(".", "") for s in mainline]
    mainline = [s.replace("/", "") for s in mainline]
    lts = [s.replace(".", "") for s in lts]
    lts = [s.replace("/", "") for s in lts]
    rc = [s.replace(".", "") for s in rc]
    rc = [s.replace("rc", "") for s in rc]
    rc = [s.replace("/", "") for s in rc]

    # give latest version
    mainline.sort()
    mainline = (mainline[-1])
    lts.sort()
    lts = (lts[-1])
    rc.sort()
    rc = (rc[-1])

    # convert back
    mainline = (str(mainline))
    mainline = mainline[:1] + '.' + mainline[1:]
    mainline = mainline[:4] + '.' + mainline[4:]
    mainline = str(mainline).replace("['", "")
    mainline = str(mainline).replace("']", "")
    lts = lts[:1] + '.' + lts[1:]
    lts = lts[:4] + '.' + lts[4:]
    lts = str(lts).replace("['", "")
    lts = str(lts).replace("']", "")
    rc = rc[:1] + '.' + rc[1:]
    rc = rc[:5] + 'rc' + rc[5:]
    rc = str(rc).replace("['", "")
    rc = str(rc).replace("']", "")

    os.system('rm file1.txt')
    return mainline, lts, rc
