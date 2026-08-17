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
                        // Creates pass.txt with zero trailing newlines, logs in, then cleans up
                        bat """
                            echo | set /p="%DOCKER_PASS%" > pass.txt
                            docker login -u %DOCKER_USER% --password-stdin < pass.txt
                            if exist pass.txt del pass.txt
                            docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                            docker push ${DOCKER_IMAGE}:latest
                        """
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
