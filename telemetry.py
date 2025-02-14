import time
import autopilot
import messages
import router
import definitions as vars

def telemetry_requestor(stop_command):
    while autopilot.state['connection'] == False and not stop_command.is_set():
        try:
            time.sleep(5)
            messages.display(messages.telemetry_process_connecting, [vars.companion_computer])
        except Exception as e:
            messages.display(messages.fatal_error, [e])
            pass
    
    if not stop_command.is_set():
        messages.display(messages.telemetry_process_connected, [vars.companion_computer])

    while not stop_command.is_set():
        try:            
            # if int(autopilot.state['altitude']) > 1:
            router.put_command(router.Command(2,'MONITOR',{'target':'MSP_ANALOG'}))
            
            router.put_command(router.Command(2,'TELEMETRY',{'target':'MSP_ALTITUDE'}))
            router.put_command(router.Command(1,'TELEMETRY',{'target':'MSP_RC'}))
            time.sleep(4)
        except:
            pass

    stopped_time = time.strftime("%H:%M:%S, %Y, %d %B", time.localtime())
    messages.display(messages.telemetry_requestor_done, [stopped_time])