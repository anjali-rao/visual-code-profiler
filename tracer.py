# extracts frame code
import datetime
import time


def write_log_to_file(log_line):
    f = open("trace_logs.txt", "a")
    f.write(log_line)
    f.close()


def add_base_logs(event, filename, line_no, method_name, l_args, g_args):
    return {
        "filename": filename,
        "line_no": line_no,
        "method_name": method_name,
        "l_args": l_args,
        "g_args": g_args,
        "event": event,
        "exc_time": time.time(),
        "cpu_time": time.process_time()
    }

def my_tracer(frame, event, arg = None):
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno
    log_data = add_base_logs(event, frame.f_code.co_filename, line_no, func_name, frame.f_locals, frame.f_globals)

    if event == "exception":
        exc_type, exc_value, exc_traceback = arg
        log_data["exc_type"] = exc_type
        log_data["exc_value"] = exc_value,
        log_data["traceback"] = exc_traceback

        write_log_to_file(f"\n {log_data}")
        return True
        # Get the stack trace as a list of frame objects

    if event == "call":
        c_method_name = frame.f_code.co_name
        arg_values = frame.f_locals
        log_data["c_method_name"] = c_method_name,
    
    write_log_to_file(f"\n {log_data}")
    return my_tracer
