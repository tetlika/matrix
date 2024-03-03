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
                    dockerImage.inside('-v $WORKSPACE:/output -u root') {
                        sh 'python3 /script.py'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
              withAWS(credentials: 'aws', region: 'us-east-1') {
                      sh 'timestamp=$(date +%s); aws s3 cp s3://matrixsuper/artifact.txt artifact.txt_${timestamp}'
                      sh 'aws s3 cp artifact.txt s3://matrixsuper/'
                      sh 'aws s3 cp artifact.txt_${timestamp} s3://matrixsuper/'
                }
            }
        }
    }
}