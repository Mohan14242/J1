pipeline{
    agent {node { label "terraform1"}}
    stages{
        stage("terraform stage"){
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-access', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    script{
                        sh '''
                        cd /home/centos/terraform-deve/module-vpc/
                        terraform init 
                        terraform plan '''
                    }
    // some block
                }
            }
        }
    }
}