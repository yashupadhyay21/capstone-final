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
                bat "docker build -t ${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                // Windows doesn't support `|| true`, so use `exit 0` to suppress errors
                bat "docker stop ${CONTAINER_NAME} || exit 0"
                bat "docker rm ${CONTAINER_NAME} || exit 0"
                bat "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:${TAG}"
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
