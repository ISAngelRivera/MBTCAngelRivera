<br />
<div align="center">
  <img src="/images/MercedesLogo.jpg" alt="Logo" width="100" height="150">
<h3 align="center">THE FORCE</h3>
  <p align="center">
    A POWER THAT ALLOWS YOU TO CONNECT WITH THE STAR WARS UNIVERSE
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## 1. About the project

**THE FORCE** is designed to interact with The Star Wars API to retrieve data, process it, and expose a new API endpoint that serves the sorted data. 

### 1.1 Project workflow 

1. **API Interaction**: The service uses the `theforceapiservice.py` to fetch data from the SWAPI's people endpoint.
2. **Data Processing**: The data is sorted by the name attribute within the service.
3. **Flask Application**: The `theforceapp.py` sets up a Flask web service that exposes an endpoint to retrieve the sorted data.
4. **Containerization**: The application is containerized using Docker `Dockerfile`, making it easy to deploy.
5. **Orchestration**: Minikube is used for deployment and scaling, with configurations provided in the `.yaml` files.
6. **Load Testing**: Load is generated using a BusyBox container `load-generator.yaml` to test the scalability of the service.


### 1.2 Project structure

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
## 2. Getting Started
### 2.1 Prerequisites
#### 2.1.1 Install Python

```sh 
# Windows
winget install Python
# Unix
sudo apt install python3
```

#### 2.1.2 Install Docker 

* Docker installation guide for **Windows** Systems: https://docs.docker.com/desktop/install/windows-install/

* Docker installation guide for **Unix** Systems: https://docs.docker.com/desktop/install/linux-install/

#### 2.1.3 Install Minikube  

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
#### 2.1.4 Ensure Minikube is running
```sh
# Check status 
minikube status
# Verify nodes 
kubectl get nodes
```

#### 2.1.5 Install Metric Server 

* Install **metric server**:
```sh
# Install Metric server 
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Installation Windows check 
kubectl get apiservices | Select-String -Pattern "metrics"
# Installation Unix check 
kubectl get apiservices | grep metrics
```

* Check **metric server** functionallity: 
```sh
# run the following commands
kubectl top nodes
kubectl top pods
```


t Setup
### 3.1 Environment setup
#### 3.1.1 Clone repository
```sh
git clone https://github.com/ISAngelRivera/MBTCAngelRivera.git
```
#### 3.1.2 Activate the virtual environment [optional]
```sh
# Windows 
.\Scripts\activate
# Unix
source Scripts/activate
```

#### 3.1.3 Install dependences
```sh 
pip install -r TheForce\Theforceservice\requirements.txt
```

#### 3.1.4 Build Docker image:
```sh
docker build -t theforce-service:latest .
```


## 4. Run APP Locally
### 4.1 Run APP using Docker
#### 4.1.1 Run Flask APP using Docker
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


#### 4.1.2 Error handling and logging
Logs will appear in your command line. To verify it's working, **refresh the URL** `http://127.0.0.1:5000/people` and check if a new log entry is generated. Also you can check logs at `TheForce\Theforceservice\logs\theforce.log`

<img src="/images/errorhandlinngdocker.jpg" alt="Error handling in command line" width="800"/>

> [!NOTE]
> Additional info about error handling configuration: **`TheForce\Theforceservice\utils\error_handling.py`**


### 4.2 Run APP using Docker Compose
> [!WARNING]
> If you have configured Docker to work through Minikube or another solution, please remember to unset it first to avoid any potential issues. 
```sh
# Windows 
& minikube -p minikube docker-env --shell powershell --unset | Invoke-Expression
# Unix 
eval $(minikube -p minikube docker-env --unset)
```
#### 4.2.1 Run APP DC
```sh
# Run APP
docker-compose up --build
# Stop APP when needed
ctrl + c
```
> [!NOTE]
> Additional info about error handling configuration: **`TheForce\Theforceservice\docker-compose.yaml`**

#### 4.2.2 Test & Error handling DC
Logs will appear in your command line. To verify it's working, **refresh the URL** `http://127.0.0.1:5000/people` and check if a new log entry is generated. Logs can be also consulted inside the container `/app/logs/thefroce.log`.

<img src="/images/appdockercompose.jpg" alt="Error handling in command line" width="" height=""/>

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

## 5. Run APP using KMinikube 
### 5.1 Previous validations
#### 5.1.1 Check Pods
We will ensure that any "**theforce**" pod is runing
```sh
# Windows 
kubectl get pods -o wide | Select-String "theforce"
# Unix
kubectl get pods -o wide | grep theforce
```
We should get a '**No resources found in default namespace.**' response

#### 5.1.2 Check images 
We verify that we dont have any previous "**theforce**" image
```sh
minikube image ls
```

#### 5.1.3 Check deployment
We check that we dont have any previous "**theforce**" service up
```sh
kubectl get deployment
```

#### 5.1.4 Check services
Ensure that we dont have any previous "**theforce**" service up
```sh
kubectl get service
```

#### 5.1.5 Check HPA 
Make sure we dont have any previous "**theforce**" image
```sh
kubectl get hpa
```

### 5.2 Configure Minikube 
#### 5.2.1 Configure Docker to work with Minikube 
```sh
# Windows
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
# Unix
eval $(minikube docker-env)
```
#### Create image in Minikube
```sh
# Create new "thefoce" image 
docker build -t theforce-service:latest .
# Check that it was created 
minikube image ls docker.io/library/theforce-service:latest
```

#### 5.2.2 Ensure Minikube is running
```sh
# Check status 
minikube status
# Verify control-plane node 
kubectl get nodes
```
<img src="/images/Theforceminikubenode.jpg" alt="Error handling in command line" width="700" height=""/>

#### 5.2.3 Deploy Application & check
```sh
# Deploy APP
kubectl apply -f deployment.yaml
# Check deployment & pods 
kubectl get deployments
kubectl get pods
```
<img src="/images/Theforcedeploymentcompleted.jpg" alt="Error handling in command line" width="700" height=""/>

#### 5.2.4 Deploy Application service & check
```sh
# Expose APP 
kubectl apply -f service.yaml
# Check service
kubectl get services
```
<img src="/images/Theforceservicerunning.jpg" alt="Error handling in command line" width="700" height=""/>

#### 5.2.5 Expose service 
```sh
# Windows
Start-Job -ScriptBlock { minikube service theforce-service }
# Unix 
minikube service theforce-service &

# Check service adding "/people" to the provided URL:Port 
```
<img src="/images/TheforceExposeservice.jpg" alt="Error handling in command line" width="700" height=""/>


### 5.3 Create HPA 
### 5.3.1 Create HPA based on CPU
```sh
# Create HPA based on CPU: 
kubectl autoscale deployment theforce-deployment --cpu-percent=50 --min=2 --max=8
#Check HPA status: 
kubectl get hpa
```
<img src="/images/TheforceHPAconfigured.jpg" alt="Error handling in command line" width="700" height=""/>

## 6. Performance test
### 6.1 Check cluster current status
```sh
# Check HPA status
kubectl get hpa
```
We should have 2 pods with a low CPU load
<img src="/images/TheforceHPAconfigured.jpg" alt="Error handling in command line" width="700" height=""/>


### 6.2 Load generator
#### 6.2.1 Deploy load generator
```sh
# Deploy load generator
kubectl apply -f load-generator.yaml
# Check is running 
kubectl get pods 
# Check logs 
kubectl logs load-generator
```
#### 6.2.2 Check autoscaling increassing pods
```sh
kubectl get hpa -w
```
<img src="/images/Theforceservicepodsincreasing.jpg" alt="Error handling in command line" width="700" height=""/>


#### 6.2.3 Stop load generator
```sh
# Delete load generator
kubectl delete pod load-generator
# Check is not running 
kubectl get pods 
```

#### 6.2.4 Check autoscaling decreassing pods
```sh
kubectl get hpa -w
```
<img src="/images/Theforceservicepodsdecreasing.jpg" alt="Error handling in command line" width="700" height=""/>


> [!NOTE]
> Once the CPU load decreases, the autoscaler may take 5 minutes or longer to scale down the replicas. This delay is designed to avoid inconsistencies in the service




<p align="right">(<a href="#readme-top">back to top</a>)</p>
