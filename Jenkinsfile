pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('test') {
            steps {
                sh 'pytest'
            }
        }

        stage('deploy') {
        	agent none

            steps {
                sh 'docker build -t sweet-api .'
                sh 'docker run -d -p 5000:80 sweet-api'
            }
        }
    }
}
