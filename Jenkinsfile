pipeline {
    agent any
    
    triggers {
     
        pollSCM('*/5 * * * *') 
    }

    stages {
        stage('Build') {
            steps {
                
                sh 'echo "Building..."'
            }
        }
        stage('Deploy') {
            steps {
              
                sh 'echo "Deploying..."'
            }
        }
    }
}