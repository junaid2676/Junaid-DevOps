pipeline {
    agent any

    environment {
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
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        powershell '$OutputEncoding = [System.Text.Encoding]::UTF8; $env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin'
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
