pipeline {
    agent { dockerfile true }
    stages {

        stage('test') {
            steps {
                sh 'pytest'
            }
        }

        stage('deploy') {
        	agent any
        	
            steps {
                sh 'docker build -t sweet-api .'
                sh 'docker run -d -p 5000:80 sweet-api'
            }
        }
    }
}
