def update_status ( status_rn ):
    updated_status_msg = None
    STATUS_DEFAULTS = ["Hey there","Fuck you Donald Trump",69]
    if status_rn != None:
        print "Your current status message is: %s" % (status_rn) + "\n"
    else:
        print 'You don\'t have any status message currently \n'
        default=raw_input("Do you want to select status from defaults? Y/N")
        if default.upper() == "N":
            new_status_msg = raw_input("Enter your status")
            if len(new_status_msg) > 0:
                STATUS_DEFAULTS.append(new_status_msg)
                updated_status_msg = new_status_msg

        elif default.upper() == "Y":
            item_position = 1
            for message in STATUS_DEFAULTS:
                print "%d.%s" %(item_position,message)
                item_position = item_position+1

            select_status = int(raw_input("Select number corresponding to the status you want to use"))
            if len(STATUS_DEFAULTS) >= select_status:
                updated_status_msg = STATUS_DEFAULTS[select_status - 1]

    return(updated_status_msg)




