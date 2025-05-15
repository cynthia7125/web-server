# Setting up an NGINX server

## 1. Install NGINX

```
brew install nginx
nginx
nginx -s reload
```


## 2. Create a Python Environment

```
python3 -m venv streamlit_env

source streamlit_env/bin/activate

pip install -r requirements.txt // Done only if you have dependencies in a file named requirements.txt
```

CMD lines should begin with the specified env name. In my case "streamlit_env"

## 3. Run Streamlit in the Background

```
nohup streamlit run app.py --server.port 8503 --server.enableCORS false --server.headless true > streamlit.log 2>&1 &

```

To verify it’s running:

```
ps aux | grep streamlit
```

## 4. Configure NGINX
Edit config file from the CMD using the nano command.
Save to a .conf file in your folder.
Access config file using:

```
sudo nano /opt/homebrew/etc/nginx/nginx.conf
```

Test the configurations using:

```
sudo nginx -t
```

Restart NGINX if successful:

```
sudo nginx -s reload
```

## Common Issues and Fixes
- **Nginx not running**:
  - Kill processes occupying ports 80 and 443:
    ```bash
    sudo lsof -i :80
    sudo lsof -i :443
    sudo kill -9 $(sudo lsof -t -i :80)
    sudo kill -9 $(sudo lsof -t -i :443)
    ```
  - Remove existing PID file and restart NGINX:
    ```bash
    sudo rm /opt/homebrew/var/run/nginx.pid
    brew services restart nginx
    ```

- **Permission Denied**:
  - Ensure you have root privileges for NGINX commands.
```

## Mistakes to Avoid
- **Incorrect Server IP**:
  Use the **virtual machine’s IP address**, not your local machine’s, as the server name in your config file.
  
- **Missing Port in IP**:
  Always include the `:PORT` extension (e.g., `192.168.1.100:8503`) to avoid WebSocket issues.
