pipeline {
    agent any
    
    triggers {
     
        pollSCM('*/3 * * * *') 
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