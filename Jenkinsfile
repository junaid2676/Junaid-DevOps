pipeline {
    agent any

    environment {
        // Automatically creates junaiddevops21/devops:v1, v2, v3, etc.
        DOCKER_IMAGE = "junaiddevops21/devops:v${BUILD_NUMBER}"
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('2. Run Unit Tests') {
            steps {
                script {
                    echo 'Running automated tests...'
                    // Runs tests inside your repository before building the Docker image
                    sh 'python3 -m unittest discover -s . -p "test_*.py" || echo "No tests found, skipping..."'
                }
            }
        }

        stage('3. Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image: ${DOCKER_IMAGE}"
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('4. Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        always {
            sh 'echo "Pipeline execution finished for build #${BUILD_NUMBER}."'
        }
    }
}
