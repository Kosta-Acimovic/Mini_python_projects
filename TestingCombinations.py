mouse=["Mechanical Mouse","Trackball Mouse","Optical Mouse","Wireless Mouse"]
keyboard=["QWERTY","QWERTZ","AZERTY"]
speakers=["Modern loudspeakers","Ceiling speakers","Soundbars","Woofers"]
monitors=["CRT","LCD","TFT","LED","Touchscreen","Plasma Screen","OLED"]

for m1 in mouse:
    for k in keyboard:
        for s in speakers:
            for m2 in monitors:
                print("I have:\n"
                      "\t",m1,"for my mouse\n"
                            "\t",k,"for my keyboard\n"
                                 "\t",s,"for my speakers\n"
                                      "\t",m2,"for my monitor\n")