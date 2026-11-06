pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
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
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
