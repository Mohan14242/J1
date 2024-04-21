pipeline{
    agent {node { label "terraform"}}
    stages{
        stage("terraform stage"){
            steps{
                script{
                    sh '''
                    pwd'''
                }
            }
        }
    }
}