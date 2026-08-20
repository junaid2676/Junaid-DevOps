pipeline {
    agent any

    stages {
        stage('1. Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('2. Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image: junaid2676/devops:v1'
                    sh 'docker build -t junaid2676/devops:v1 .'
                }
            }
        }
        stage('3. Push to Docker Hub') {
            steps {
                sh 'docker push junaid2676/devops:v1'
            }
        }
    }

    post {
        always {
            sh 'echo "Pipeline execution finished."'
        }
    }
}
