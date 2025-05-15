# Setting up an NGINX server

## Install NGINX

```
brew install nginx
nginx
nginx -s reload
```

## Create an env

```
python3 -m venv streamlit_env

source streamlit_env/bin/activate

pip install -r requirements.txt // Done only if you have dependencies in a file named requirements.txt
```

CMD lines should begin with the specified env name. In my case "streamlit_env"

## Run my streamlit page in the background

```
nohup streamlit run app.py --server.port 8503 --server.enableCORS false --server.headless true > streamlit.log 2>&1 &

```

Since we can not run it on our browser becasue it is running in the created environment and not our locan machine we use the below command to check that it is up and running:

```
ps aux | grep streamlit
```

## Configure nginx

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

If successful, restart the nginx server.

# Issues I run into

1. Nginx was not running:

```
nginx (homebrew.mxcl.nginx)
Running: ✘
Loaded: ✔
Schedulable: ✘
```

- To fix it in my case I run:

```
sudo lsof -i :80
sudo lsof -i :443
sudo kill -9 `sudo lsof -t -i :80`
sudo kill -9 `sudo lsof -t -i :443`
```

- This sort of restarted my environment and when I started nginx this is what I got:

```
nginx (homebrew.mxcl.nginx)
Running: ✔
Loaded: ✔
Schedulable: ✘
User: root
```

2. Permission Denied

```
web server % nginx
nginx: [emerg] open() "/opt/homebrew/var/run/nginx.pid" failed (13: Permission denied)
```

- To fix the above in my case I run:

```
sudo rm /opt/homebrew/var/run/nginx.pid

brew services restart nginx
```

# Mistakes I Made  

1. **Using my local machine's IP address as the server name in the config file instead of the virtual machine's IP.**  
   - The site was always unreachable, and I couldn’t find a solution online. Eventually, I realized that my IP kept changing, which led me to focus on the IP address itself. That’s when I noticed the issue—my local machine’s IP was incorrect, and it was never going to work.  

2. **Running the IP without the `:PORT` extension.**  
   - This caused WebSocket issues, making the app continuously load without displaying any content. Adding the correct port resolved the issue. 


# New Collaborators

   - Hello everyone my name is Shane and I am a new collaborator on the project. I hope you enjoy running it and I'm happy to be onboard.