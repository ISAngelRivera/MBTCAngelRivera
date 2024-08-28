<br />
<div align="center">
  <img src="/images/MercedesLogo.jpg" alt="Logo" width="100" height="150">
<h3 align="center">THE FORCE</h3>
  <p align="center">
    A POWER THAT ALLOWS YOU TO CONNECT WITH THE STAR WARS UNIVERSE
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## About the project

**THE FORCE** is designed to interact with The Star Wars API to retrieve data, process it, and expose a new API endpoint that serves the sorted data. 

### Project workflow 

1. **API Interaction**: The service uses the `theforceapiservice.py` to fetch data from the SWAPI's people endpoint.
2. **Data Processing**: The data is sorted by the name attribute within the service.
3. **Flask Application**: The `theforceapp.py` sets up a Flask web service that exposes an endpoint to retrieve the sorted data.
4. **Containerization**: The application is containerized using Docker `Dockerfile`, making it easy to deploy.
5. **Orchestration**: Kubernetes is used for deployment and scaling, with configurations provided in the `.yaml` files.
6. **Load Testing**: Load is generated using a BusyBox container `load-generator.yaml` to test the scalability of the service.


### Project structure

```
MBTCAngelRivera/
│
├── images/
│   └── MercedesLogo.jpg       # An image used in the documentation or for visual representation
│
├── TheForce/
│   ├── Test/
│   │   ├── test_theforceapiservice.py   # Unit tests for theforceapiservice.py
│   │   └── test_theforceapp.py          # Unit tests for theforceapp.py
│
├── Theforceservice/
│   ├── service/
│   │   ├── __init__.py         # Marks this directory as a Python package
│   │   └── theforceapiservice.py   # Handles interactions with The Star Wars API
│   │
│   └── utils/
│   │   ├── __init__.py         # Marks this directory as a Python package
│   │   └── error_handling.py   # Centralized error handling logic for the Flask app
│   │
│   ├── docker-compose.yaml        # Docker Compose configuration for running the application and its dependencies
|   ├── Dockerfile                 # Dockerfile to build the application's Docker image
|   ├── deployment.yaml            # Kubernetes deployment configuration
|   ├── load-generator.yaml        # Kubernetes configuration for the load generator pod
|   ├── service.yaml               # Kubernetes service configuration for exposing the application
|   ├── theforceapp.py             # Main entry point of the Flask application
|   ├── pyvenv.cfg                 # Configuration file for the Python virtual environment
|   └── README.md                  # Project documentation and usage instructions
```



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
#### Install Python

```sh 
# Windows
winget install Python
# Unix
sudo apt install python3
```

#### Install Docker 

* Docker installation guide for **Windows** Systems: https://docs.docker.com/desktop/install/windows-install/

* Docker installation guide for **Unix** Systems: https://docs.docker.com/desktop/install/linux-install/

#### Install Minikube  

* Download page for **Windows** & **Unix Systems**: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download

> [!NOTE]
> Sometimes work with Minikube environments can produce TLS errors that you can avoid by following the next steps.  
```sh
# show config
kubectl edit deployment metrics-server -n kube-system

# edit config
spec:
  containers:
  - name: metrics-server
    image: k8s.gcr.io/metrics-server/metrics-server:v0.5.0
    args:
    - --cert-dir=/tmp
    - --secure-port=4443
    - --kubelet-preferred-address-types=InternalIP,Hostname,ExternalIP
    - --kubelet-use-node-status-port
    - --kubelet-insecure-tls

#restart depployment to apply changes if needed
kubectl rollout restart deployment metrics-server -n kube-system
```
#### Ensure Minikube is running
```sh
# Check status 
minikube status
# Verify nodes 
kubectl get nodes
```

#### Install Metric Server 

* Install **metric server**:
```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
* Check **metric server** installation: 
```sh
# If the Metric Server was installed successfully, you should be able to run the following commands
kubectl top nodes
kubectl top pods
```

## Project Setup
### Environment setup
#### Clone repository
```sh
git clone https://github.com/ISAngelRivera/MBTCAngelRivera.git
```
#### Activate the virtual environment [optional]
```sh
# Windows 
.\Scripts\activate
# Unix
source Scripts/activate
```

#### Install dependences
```sh 
pip install -r TheForce\Theforceservice\requirements.txt
```

#### Build Docker image:
```sh
docker build -t theforce-service:latest .
```


## Run APP Locally
### Run APP using Docker
#### Run Flask APP using Docker
* Run Flask:
```sh
#[OPTIONAL: In this example we used the virtual environment python to avoid Issues]
MBTCAngelRivera\TheForce\Scripts\python.exe .\theforceapp.py

# Stop APP when needed
ctrl + c
```

* Check functionality:
```sh
#Check URL
http://127.0.0.1:5000/people
```

<img src="/images/localappworking.jpg" alt="Error handling in command line" width="300" height="500"/>

> [!NOTE]
> Additional info about Docker configuration: **`TheForce\Theforceservice\theforceapp.py`**


#### Error handling and logging
Logs will appear in your command line. To verify it's working, **refresh the URL** `http://127.0.0.1:5000/people` and check if a new log entry is generated. Also you can check logs at `TheForce\Theforceservice\logs\theforce.log`

<img src="/images/errorhandlinngdocker.jpg" alt="Error handling in command line" width="800"/>

> [!NOTE]
> Additional info about error handling configuration: **`TheForce\Theforceservice\utils\error_handling.py`**


### Run APP using Docker Compose
> [!WARNING]
> If you have configured Docker to work through Minikube or another solution, please remember to unset it first to avoid any potential issues. 
```sh
# Windows 
& minikube -p minikube docker-env --shell powershell --unset | Invoke-Expression
# Unix 
eval $(minikube -p minikube docker-env --unset)
```
#### Run APP DC
```sh
# Run APP
docker-compose up
# Stop APP when needed
ctrl + c
```
> [!NOTE]
> Additional info about error handling configuration: **`TheForce\Theforceservice\docker-compose.yaml`**

#### Test & Error handling DC
Logs will appear in your command line. To verify it's working, **refresh the URL** `http://127.0.0.1:5000/people` and check if a new log entry is generated. Logs can be also consulted inside the container `/app/logs/thefroce.log`.

<img src="/images/appdockercompose.jpg" alt="Error handling in command line" width="500" height="400"/>

> [!TIP]
> There are some command that may help you.
```sh
# Log in to the container by replacing 'containerid' value
docker exec -it 'containerid' /bin/bash
# Check "app" folder to ensure that your APP was deployed 
ls -alh /app
# Check the application logs inside the container from outside
docker exec -it 'containerid' cat /app/logs/thefroce.log
```

### Run APP using Kubernetes
#### Configure Docker to work with Minikube 

```sh
# Windows
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
# Unix
eval $(minikube docker-env)
```

#### Ensure Minikube is running
```sh
# Check status 
minikube status
# Verify nodes 
kubectl get nodes
```
#### Deploy Application & check
```sh
# Deploy APP
kubectl apply -f deployment.yaml
# Check deployment & pods 
kubectl get deployments
kubectl get pods
```

#### Expose Application & check
```sh
# Expose APP 
kubectl apply -f service.yaml
# Check service
kubectl get services
```
#### Create HPA 
```sh
# Create HPA based on CPU: 
kubectl autoscale deployment theforce-deployment --cpu-percent=50 --min=2 --max=8
#Check HPA status: 
kubectl get hpa
```







```
#restart depployment to apply changes if needed
kubectl rollout restart deployment metrics-server -n kube-system
```

**Check metric-server install on Windows**: 
```sh
#Check installation
kubectl get apiservices | Select-String -Pattern "metrics"
```

**Check metric-server install on Unix**: 
```sh
#Check installation
kubectl get apiservices | grep metrics

#Check data from pods
kubectl top pods
```






## Performance test
### Check cluster current status
* 
Image


### Load generator
#### Start load generator
```sh
# Deploy load pod
kubectl apply -f service.yaml
# Check is running without errors
kubectl get pods -l app=load-generator
# Check logs 
kubectl logs load-generator
```



#### Stop load generator
```sh
kubectl delete pod load-generator
```

#### Number of replics decreasing



<p align="right">(<a href="#readme-top">back to top</a>)</p>


