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
                        // Strips all hidden spaces, newlines, and CRLF characters automatically
                        powershell '''
                            $user = $env:DOCKER_USER.Trim()
                            $pass = $env:DOCKER_PASS.Trim()
                            [System.IO.File]::WriteAllText("pass.txt", $pass)
                            Get-Content pass.txt | docker login -u $user --password-stdin
                            Remove-Item pass.txt -ErrorAction SilentlyContinue
                        '''
                        
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
