pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/your-username/your-repo.git'
        BRANCH = 'main'
        COMPOSE_FILE = 'docker-compose.yml'
    }   

    stages {
        stage('Setup') {
            steps {
                script{
                    sh "git clone -b $BRANCH $REPO_URL"
                }
            }
        }
        stage('Build') {
            steps {
                script{
                    sh "cd your-repo && docker-compose down"
                    sh "docker-compose -d up"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
