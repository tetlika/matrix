pipeline {
    agent any
    
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch name')
    }

    triggers {
     
        pollSCM('*/3 * * * *') 
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: params.BRANCH]],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          submoduleCfg: [],
                          userRemoteConfigs: [[url: 'https://github.com/tetlika/matrix.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    def dockerImage = docker.build('my_image:latest')
                }
            }
        }
        stage('Deploy') {
            steps {
              
                sh 'echo "Deploying..."'
            }
        }
    }
}