pipeline {
    agent any

    environment {
        // Defines your image name using your Docker Hub username
        DOCKER_IMAGE = 'junaid2676/devops'
        // Uses the Jenkins build number as a unique tag (e.g., v1, v2, v3)
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                // Gets the latest code from your repository
                checkout scm
            }
        }

     stage('2. Build Docker Image') {
    steps {
        script {
            echo "Building Docker Image: ${DOCKER_IMAGE}:${IMAGE_TAG}"
            bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t junaid2676/devops:v1 .'
        }
    }
}

        stage('3. Push to Docker Hub') {
            steps {
                script {
                    // 'docker-hub-credentials' is the ID of your login stored inside Jenkins
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        bat "docker push ${DOCKER_IMAGE}:${IMAGE_TAG}"
                        bat "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            // Cleans up local Docker images on the Jenkins server to save space
            bat "docker logout"
        }
    }
}
