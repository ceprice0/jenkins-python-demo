pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest --junitxml=results.xml'
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
            junit testResults: 'results.xml', allowEmptyResults: true
        }
    }
}
