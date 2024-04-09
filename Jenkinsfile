pipeline {
    agent { node { label 'agent3' }}
    
    environment {
        AWS_BUCKET = 'mohan14242'
        ARTIFACT_NAME = 'cat.zip'
    }
    
    stages {
        stage('Build Artifact') {
            steps {
                dir('.') {
                    script {
                        // Print current directory
                        sh 'pwd'
                        // Zip files in current directory
                        sh "zip -r ${env.ARTIFACT_NAME} ./*"
                    }
                }
            }
        }
        
        stage('Upload Artifact to S3') {
            steps {
                script {
                    // Print environment variables
                    echo "AWS_BUCKET: ${env.AWS_BUCKET}"
                    echo "ARTIFACT_NAME: ${env.ARTIFACT_NAME}"
                    // Upload artifact to S3
                    withCredentials([awsSecret(credentialsId: 'aws-mohan', variable: 'AWS_CREDENTIALS')]) {
                        sh "aws s3 cp ${env.ARTIFACT_NAME} s3://${env.AWS_BUCKET}/${env.ARTIFACT_NAME}" || error('Failed to upload artifact to S3')
                    }
                }
            }
        }
    }
}
