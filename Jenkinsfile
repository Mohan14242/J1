pipeline{
    agent any
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