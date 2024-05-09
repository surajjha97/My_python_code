import psutil
def is_malicious_process_running():
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] == 'powershell.exe':
            cmdline = proc.info['cmdline']
            if any(arg in cmdline for arg in ['-nop', '-noni', 'invoke-expression', 'iex', '.downloadstring', 'downloadfile']):
                return True
    return False

if is_malicious_process_running():
    print("Malicious process detected!")
else:
    print("No malicious process detected.")