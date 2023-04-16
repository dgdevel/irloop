import time
import irsdk

def iracing_update_connection_state(ir, ir_running):
    if ir_running and not (ir.is_initialized and ir.is_connected):
        ir_running = False
        ir.shutdown()
        print('iRacing disconnected')
    elif not ir_running and ir.startup() and ir.is_initialized and ir.is_connected:
        ir_running = True
        print('iRacing connected')
    return ir_running

def main_thread():
    ir = irsdk.IRSDK()
    ir_running = False
    while True:
        ir_running = iracing_update_connection_state(ir, ir_running)
        if ir_running:
            ir.freeze_var_buffer_latest()
            replay_position_from_end = ir['ReplayFrameNumEnd']
            if replay_position_from_end == 1:
                ir.replay_set_play_position()
                ir.replay_set_play_speed(1)
        time.sleep(1) # update once per second

if __name__ == '__main__':
    main_thread()
