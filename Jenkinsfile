pipeline{
    agent any 
    stages{
        stage("getting the s3 bucke namees"){
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-mohan', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
    // some block
            sh ' aws s3 ls'
        }
        }
        }
    }
}