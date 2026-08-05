Here is a plain-English explanation of how this `Jenkinsfile` works, broken down by its main sections:

---

### **1. Core Setup & Environment**

```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'junaid2676/devops'
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

```

* **`pipeline { ... }`**: Tells Jenkins that everything inside these brackets is part of an automated workflow.
* **`agent any`**: Directs Jenkins to run this job on any available worker machine or terminal connected to Jenkins.
* **`environment { ... }`**: Defines reusable variables so you don't have to re-type them later:
* **`DOCKER_IMAGE`**: Sets your Docker Hub repository path (`junaid2676/devops`).
* **`IMAGE_TAG`**: Uses Jenkins' internal `${BUILD_NUMBER}` variable to automatically create a unique version tag every time the pipeline runs (e.g., Run #1 becomes `v1`, Run #2 becomes `v2`).



---

### **2. Stage 1: Checkout Code**

```groovy
stage('1. Checkout Code') {
    steps {
        checkout scm
    }
}

```

* **`checkout scm`**: Stands for **Source Control Management**. It instructs Jenkins to connect to your GitHub repository and download the latest code (your `Dockerfile`, `Junaid.py`, and `README.md`) onto the build server.

---

### **3. Stage 2: Build Docker Image**

```groovy
stage('2. Build Docker Image') {
    steps {
        script {
            echo "Building Docker Image: ${DOCKER_IMAGE}:${IMAGE_TAG}"
            sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
            sh "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
        }
    }
}

```

* **`sh "docker build ..."`**: Runs the standard build command inside the terminal, creating an image tagged with the build number (e.g., `junaid2676/devops:v1`).
* **`sh "docker tag ..."`**: Creates a second copy tagged as `:latest`. This ensures users can always pull the newest version without needing to know the specific version number.

---

### **4. Stage 3: Push to Docker Hub**

```groovy
stage('3. Push to Docker Hub') {
    steps {
        script {
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                sh "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE}:latest"
            }
        }
    }
}

```

* **`withCredentials(...)`**: Securely fetches your saved Docker Hub credentials from Jenkins' secure storage using the ID `'docker-hub-credentials'`. It temporarily maps your username to `$DOCKER_USER` and password to `$DOCKER_PASS` without exposing them in plain text.
* **`docker login ...`**: Log in to Docker Hub via the command line using those credentials.
* **`docker push ...`**: Uploads both the versioned image (e.g., `v1`) and the `latest` image to your Docker Hub repository online.

---

### **5. Post-Build Cleanup**

```groovy
post {
    always {
        sh "docker logout"
    }
}

```

* **`post { always { ... } }`**: Tells Jenkins to execute this step no matter what happens (even if the build succeeds or fails).
* **`sh "docker logout"`**: Logs out of Docker Hub on the server to prevent unauthorized access.
