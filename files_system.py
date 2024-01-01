import os

class Server:
    services_path = "/etc/systemd/system"

    def add_service(self, service_name):
        os.system(f"cd {self.services_path}")
        config = f'''[Unit]
Description=Telegram bot '{service_name}'
After=syslog.target
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/usr/local/bin/bots/{service_name}
ExecStart=/usr/bin/python3 /usr/local/bin/{service_name}/main.py
RestartSec=10
Restart=always
 
[Install]
WantedBy=multi-user.target'''
        service_config = open(f"{self.services_path}/{service_name}", "w+")
        service_config.write(config)
        service_config.close()

        os.system("systemctl daemon-reload")
        os.system(f"systemctl enable {service_name}")
        os.system(f"systemctl start {service_name}")
        os.system(f"systemctl status {service_name}")
    
    def stop_service(self, service_name):
        result = os.system(f"systemctl stop {service_name}")
        return result
    
    def start_service(self, service_name):
        result = os.system(f"systemctl start {service_name}")
        return result
    
    def restart_service(self, service_name):
        result = os.system(f"systemctl start {service_name}")
        return result
