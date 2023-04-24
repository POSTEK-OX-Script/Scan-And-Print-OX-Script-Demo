import ox_script

# The following code is used to initialize the UI on the printer
controller = UIInit(
    UIPage(
        UIText(name="Barcode One:", value="--"),
        UIText(name="Barcode Two", value="--"),
    ),
    # Setting require_execute_confirmation to False will allow the script to run without the need to press the execute button on the printer
    require_execute_confirmation=False,
)

#defines a list to store the two input barcodes, feel free to change the length of the list based on the number of scans per print
data = ['','']
#defines a variable to keep track of the number of scans
time = 0

while True:
    #Tries to read data from the usbhost port, if there is no data, it returns -1
    cmd = PTK_GetPortData(PORT_USBHOST, timeout=100)
    if cmd != -1:
        #Updates the UI with the scanned data
        controller['Widget_' + str(time%2 +1)].update(cmd)
        data[time%2] = cmd
        time += 1
        
        #After two successful scans, print the template barcode, the template file is command1.txt
        if time % 2 == 0 and time != 0:
            #Command1.txt is the label template file where we defined two input fields which we will update with the scanned data
            cmdd = update_all_form_variables(
                'command1.txt',
                Input1=data[0],
                Input2=data[1],
            )
            #Sends the command to the printer to initate printing
            PTK_SendCmdToPrinter(cmdd)
            
        elif time % 2 == 1 and time != 0:
           #After scanning the first barcode, the second input field is cleared
           controller['Widget_' + str(time%2)].update('--')
