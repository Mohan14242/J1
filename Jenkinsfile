pipeline{
    agent {node { label "terraform"}}
    stages{
        stage("terraform stage"){
            steps{
                script{
                    sh '''
                    pwd
                    cd /home/centos/terraform-deve
                    cd  module-vpc
                    pwd
                    ls -l
                    '''
                }
            }
        }
    }
}