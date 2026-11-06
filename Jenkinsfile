pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t snake-game:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker tag snake-game:latest calum1/snake-game:latest'
                sh 'docker push calum1/snake-game:latest'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}

