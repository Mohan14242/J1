pipeline{
    agent any 
      environment {
        AWS_BUCKET = 'mohan14242'
        ARTIFACT_NAME = 'cat.zip'
    }
    stages{
        stage("building stage"){
            steps{
                sh '''
                pwd  
                ls -l
                zip -r cat.zip ./*
                '''
            }
        }
        stage("getting the s3 bucke namees"){
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-mohan', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
    // some block
            sh ' aws s3 cp ${env.ARTIFACT_NAME} s3://${env.AWS_BUCKET}/${env.ARTIFACT_NAME}'
        }
        }
        }
    }
}