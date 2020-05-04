pipeline {
    agent any
    stages {	
    	agent { dockerfile true }


        stage('test') {
            steps {
                sh 'pytest'
            }
        }

        stage('deploy') {

            steps {
            	sh 'echo starting build'
                sh 'docker build -t sweet-api .'

                sh 'echo starting run'
                sh 'docker run -d -p 5000:80 sweet-api' 
            }
        }
    }
}