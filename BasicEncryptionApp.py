def encrypted():
    m = input("Write message you want to encrypt:\t")
    encryption = ""
    for el in m:
        if el in "Aa":
            encryption = encryption + "lo"
        elif el in "Bb":
            encryption = encryption + "aq"
        elif el in "Cc":
            encryption = encryption + "a"
        elif el in "Dd":
            encryption = encryption + "c"
        elif el in "Ee":
            encryption = encryption + "3]"
        elif el in "Ff":
            encryption = encryption + "[g"
        elif el in "Gg":
            encryption = encryption + "ere"
        elif el in "Hh":
            encryption = encryption + "pd"
        elif el in "Ii":
            encryption = encryption + "4d"
        elif el in "Jj":
            encryption = encryption + "?ds"
        elif el in "Kk":
            encryption = encryption + "="
        elif el in "Ll":
            encryption = encryption + "r1r"
        elif el in "Mm":
            encryption = encryption + "bg="
        elif el in "Nn":
            encryption = encryption + "q"
        elif el in "Oo":
            encryption = encryption + "xz"
        elif el in "Pp":
            encryption = encryption + "{)"
        elif el in "Qq":
            encryption = encryption + "(}"
        elif el in "Rr":
            encryption = encryption + ","
        elif el in "Ss":
            encryption = encryption + ".."
        elif el in "Tt":
            encryption = encryption + "`"
        elif el in "Uu":
            encryption = encryption + "~a"
        elif el in "Vv":
            encryption = encryption + "ss"
        elif el in "Ww":
            encryption = encryption + "lf"
        elif el in "Xx":
            encryption = encryption + "m~"
        elif el in "Yy":
            encryption = encryption + "/s"
        elif el in "Zz":
            encryption = encryption + ":"
        elif el in "Šš":
            encryption = encryption + ";"
        elif el in "Đđ":
            encryption = encryption + "9d"
        elif el in "Čč":
            encryption = encryption + "kje"
        elif el in "Ćć":
            encryption = encryption + "78"
        elif el in "Žž":
            encryption = encryption + "2."
    return encryption
