pipeline {
    agent any
    stages {	
    	
        stage('test') {
	        agent { dockerfile true }
    
            steps {
                sh 'pytest'
            }
        }

        stage('deploy') {

            steps {
            	sh 'echo starting build'
                sh 'docker build -t sweet-api .'

                sh 'stopping current container'
                sh 'docker kill $(docker ps -a -q  --filter ancestor=sweet-api)'

                sh 'echo starting run'
                sh 'docker run -d -p 5000:80 sweet-api' 
            }
        }
    }
}