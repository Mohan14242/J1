pipeline {
    agent { node { label 'agent3'}}
    
    environment {
        // Define the AWS S3 bucket name and artifact name
        AWS_BUCKET = 'mohan14242'
        ARTIFACT_NAME = 'cat.zip'
    }
    
    stages {
        stage('Build Artifact') {
            steps {
                sh '''
                zip -r cat.zip ./*
                '''
                // Your build steps here to create the artifact
                //e build command, replace it with your actual build command
            }
        }
        stage('Upload Artifact to S3') {
            steps {
                // Upload the artifact to AWS S3 using AWS CLI
                script {
                    sh "aws s3 cp ${ARTIFACT_NAME} s3://${AWS_BUCKET}/${ARTIFACT_NAME}"
                }
            }
        }
    }
}
