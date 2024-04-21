pipeline{
    agent {node { label "terraform1"}}
    stages{
        stage("terraform stage"){
            steps{
                script{
                    sh '''
                    sudo labauto

                    git clone https://github.com/Mohan14242/terraform-deve.git
                    cd terraform-deve
                    cd module-vpc 
                    terraform init 
                    terraform plan 
                    '''
                }
            }
        }
    }
}