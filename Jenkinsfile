pipeline {
    agent any

    environment {
        // Keeps System32, PowerShell, and Docker Desktop in PATH
        PATH = "C:\\Windows\\System32;C:\\Windows\\System32\\WindowsPowerShell\\v1.0;C:\\Users\\LAPTOP MART\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
        
        DOCKER_IMAGE = 'junaid2676/devops'
        IMAGE_TAG = 'v1'
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('2. Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image: ${DOCKER_IMAGE}:${IMAGE_TAG}"
                    bat "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                    bat "docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }

        stage('3. Push to Docker Hub') {
            steps {
                script {
                    // Native Jenkins Registry handling (Bypasses CMD/PowerShell string issues)
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        bat "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                        bat "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            bat "docker logout"
        }
    }
}
