pipeline {
    agent any

    environment {
        IMAGE_NAME = 'yash'
        TAG = 'latest'
        CONTAINER_NAME = 'yash_app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yashupadhyay21/capstone-final.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop & remove old container if exists
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // Run new container
                    sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${TAG}"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
