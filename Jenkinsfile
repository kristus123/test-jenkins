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
                sh 'docker-compose up --build -d' 
            }
        }
    }
}