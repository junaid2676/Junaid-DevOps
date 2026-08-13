pipeline {
    agent any

    environment {
        // 1. Inject Docker Desktop executable path directly into Windows environment
        PATH = "C:\\Users\\LAPTOP MART\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
        
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
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        // 2. PowerShell handles secret variables in memory safely without CMD echo corruption
                        powershell '$env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin'
                        
                        powershell "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                        powershell "docker push ${DOCKER_IMAGE}:latest"
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
