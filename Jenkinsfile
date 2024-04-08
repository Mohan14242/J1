pipeline{
    agent { node{ label 'agent1'}}
    stages{
        stage("test stage"){
            steps{
                script{
                    sh 'ls -la'
                }
            }
        }
    }
}