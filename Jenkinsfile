pipeline{
    agent { node{ label 'agent1'}}
    stages{
        stage("test stage"){
            steps{
                script{
                    sh 'npm install'
                }
            }
        }
        stage("sonar scanner"){
            steps{
                script{
                    sh 'sonar-scanner'
                }
            }
        }
    }
}