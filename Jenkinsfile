pipeline {
    agent any

    environment {
        // Force the exact path to Docker Desktop directly inside the build environment
        PATH = "C:\\Users\\LAPTOP MART\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
        
        DOCKER_IMAGE = 'junaid2676/devops'
        IMAGE_TAG = "v${BUILD_NUMBER}"
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
                // Direct login without piping avoids Windows CMD echo bugs
                bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                
                bat "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                bat "docker push ${DOCKER_IMAGE}:latest"
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
