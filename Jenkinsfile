pipeline {
    agent { node { label 'agent3' }}
    
    environment {
        AWS_BUCKET = 'mohan14242'
        ARTIFACT_NAME = 'cat.zip'
    }
    
    stages {
        stage('Build Artifact') {
            steps {
                dir('.') { // Change directory to the location of your files
                    sh '''
                    pwd
                    zip -r ${ARTIFACT_NAME} ./*
                    '''
                }
            }
        }
        
        stage('Upload Artifact to S3') {
            steps {
                script {
                    withCredentials([awsSecret(credentialsId: 'aws-mohan', variable: 'AWS_CREDENTIALS')]) {
                        sh "aws s3 cp ${ARTIFACT_NAME} s3://${AWS_BUCKET}/${ARTIFACT_NAME}"
                    }
                }
            }
        }
    }
}
